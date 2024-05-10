import re

obj_dic = {}

class object:
    def __init__(self, x, y, z, name):
        self.x = x*1.00
        self.y = y*1.00
        self.z = z*1.00
        self._name = name #NOTE Must match the name assigned to the object in the simulation environment

    def name(self):
        return self._name


class action_module(object):

    def initial_module():
        string = r"{'action': 'MoveJ', 'value': {'joint1': 0.0, 'joint2': 0.0, 'joint3': 0.0, 'joint4': 0.0, 'joint5': 0.0, 'joint6': 0.0}, 'speed': 1.0}" #Don't need a test
        return string

    def initialize_ee(ee):
        # ee location based on this function
        ee.x = 0.54545
        ee.y = 0.0007955
        ee.z = 0.62942
        string = r"{'action': 'MoveJ', 'value': {'joint1': -58.10, 'joint2': 25.75, 'joint3': 27.17, 'joint4': -63.59, 'joint5': -71.41, 'joint6': 77.67}, 'speed': 1.0}"
        return string

    def pre_grasp_module(obj,ee):
        # Pre-grasp (0.1 (z-axis) above the object)
        string = f"{{'action': 'MoveL', 'value': {{'movex': {obj.x-ee.x}, 'movey': {obj.y-ee.y}, 'movez': {obj.z-ee.z+0.1}}}, 'speed': 1.0}}"
        ee.x = obj.x-ee.x
        ee.y = obj.y-ee.y
        ee.z = obj.z-ee.z+0.1
        return string

    def move_down_module(ee):
        # Grasp (this sets the values to be inside the object?)
        string = r"{'action': 'MoveL', 'value': {'movex': 0.0, 'movey': 0.0, 'movez': -0.1}, 'speed': 1.0}"
        ee.z = ee.z - 0.1
        return string
    
    def attach_module(obj):
        # Attach #NOTE if this fails in the simulation, perhaps the name of the endeffector is wrong as this
        # assumes that all end_effectors are called EE_egp64
        string = f"{{'action': 'Attach', 'value': {{'object': '{obj.name()}', 'endeffector': 'EE_egp64'}}}}"
        return string
    
    def move_up_module(ee):
        # We need to move up after grasping to avoid collision
        string = r"{'action': 'MoveL', 'value': {'movex': 0.00, 'movey': 0.0, 'movez': 0.1}, 'speed': 1.0}"
        ee.z = ee.z + 0.1
        return string
    
    def detach_module(obj):
        string = f"{{'action': 'Detach', 'value': {{'object': '{obj.name()}'}}}}"
        return string
    
    def close_module():
        return r"{'action': 'GripperClose'}" #Don't need a test
    
    def open_module():
        return r"{'action': 'GripperOpen'}" #Don't need a test
    
    def above_new_position(ee,x,y,z):
        string = f"{{'action': 'MoveL', 'value': {{'movex': {x-ee.x}, 'movey': {y-ee.y}, 'movez': {z-ee.z+0.1}}}, 'speed': 1.0}}"
        ee.x = x-ee.x
        ee.y = y-ee.y
        ee.z = z-ee.z+0.1
        return string

def generate_instruction_set(instructions, save_file):
    target_object = obj_dic[instructions['what']] # Here we access the object
    task = instructions['how']
    location = instructions['location']
    action_list = []
    model = action_module
    match task:
        case 'move':
            # Currently we only go here
            #init
            action_list.append(model.initial_module())
            action_list.append(model.initialize_ee(obj_dic['ee']))
            #pregrasp
            action_list.append(model.pre_grasp_module(target_object,obj_dic['ee']))
            #grasp
            action_list.append(model.move_down_module(obj_dic['ee']))
            #attach
            action_list.append(model.attach_module(target_object))
            #moveup
            action_list.append(model.move_up_module(obj_dic['ee']))
            #newlocation
            if location['precise'] == 'True':
                # Precise location logic here:
                ""
            else: # Not precise:
                if location['relation'] == 'None':
                    result = move_with_respect_to(target_object, location['direction'], distance_to_float(location['distance']))
                    action_list.append(result[0])
                    action_list.append(result[1])
                else: #We have to move in relation to the other object (location['relation'])
                    result = move_with_respect_to(obj_dic[location['relation']], location['direction'], distance_to_float(location['distance']))
                    action_list.append(result[0])
                    action_list.append(result[1])
            #detach
            action_list.append(model.detach_module(target_object))
            #init
            action_list.append(model.move_up_module(obj_dic['ee']))
            action_list.append(model.initial_module())
        case 'some other action': 
            ""# This is a place-holder for future tasks, but a similar implementation would made here as above

    # Open the file in write mode
    with open(save_file, 'w') as file:
        # Iterate over the list and write each element to a separate line in the file
        for line in action_list:
            file.write(line + '\n')


def distance_to_float(distance):
    ''' 
    distance: String (for example 10 cm)
    return: float (0.1)
    '''
    value, unit = distance.split()
    value = float(value)

    if unit == 'cm':
        value /= 100.0

    return value


def move_with_respect_to(relation, direction, distance):
    '''
        parameter relation: type object (either some other object or itself)
        parameter direction: type string
        parameter action_module: type action_module

        return: String

        This function is basically for generating the target location of a object being moved
        and returning the string that corresponds that action
    '''

    list_of_strings = []
    am = action_module
   
    match direction:
        case 'forward':
            list_of_strings.append(am.above_new_position(obj_dic['ee'],relation.x,relation.y+distance,relation.z))
            list_of_strings.append(am.move_down_module(obj_dic['ee']))
        case 'backwards':
            list_of_strings.append(am.above_new_position(obj_dic['ee'],relation.x,relation.y-distance,relation.z))
            list_of_strings.append(am.move_down_module(obj_dic['ee']))
        case 'right':
            list_of_strings.append(am.above_new_position(obj_dic['ee'],relation.x+distance,relation.y,relation.z))
            list_of_strings.append(am.move_down_module(obj_dic['ee']))
        case 'left':
            list_of_strings.append(am.above_new_position(obj_dic['ee'],relation.x-distance,relation.y,relation.z))
            list_of_strings.append(am.move_down_module(obj_dic['ee']))
        case 'behind': #same as backwards but a different object will be passed to the function
            list_of_strings.append(am.above_new_position(obj_dic['ee'],relation.x,relation.y-distance,relation.z))
            list_of_strings.append(am.move_down_module(obj_dic['ee']))
        case 'in front': # same as forward but a different object will be passed to the function
            list_of_strings.append(am.above_new_position(obj_dic['ee'],relation.x,relation.y+distance,relation.z))
            list_of_strings.append(am.move_down_module(obj_dic['ee']))
        case '':
            ""
    
    return list_of_strings

def parse_ros2_command(command):

    params = {"name": None, "x": None, "y": None, "z": None}
    
    params["name"] = re.search(r'--name\s+"?([^"\s]+)"?', command)
    params["x"] = re.search(r'--x\s+([0-9\.]+)', command)
    params["y"] = re.search(r'--y\s+([0-9\.]+)', command)
    params["z"] = re.search(r'--z\s+([0-9\.]+)', command)
    
    for key in params:
        if params[key]:
            params[key] = params[key].group(1)
            if key in ["x", "y", "z"]: 
                params[key] = float(params[key])

    return params

def items_setup(items_instruction):
    items = parse_ros2_command(items_instruction)
    item = object(items['x'],items['y'],items['z'],items['name'])
    obj_dic[items['name']] = item

    return obj_dic
        
def processor(items_instruction, move_instruction):
    '''
    Input Example:
        items_instruction: 'ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "apple.urdf" --name "apple" --x 4.0 --y 5.0 --z 6.0'
        move_instruction: {'what': 'cup',
        'how': 'move',
        'location': {'precise': 'False',
        'relation': 'box',
        'direction': 'forward',
        'distance': '10 cm'}
    }
    '''

    # Create the objects:
    for instruction in items_instruction:
        _ = items_setup(instruction)
    
    # Create the end-effector
    ee_x = 0.54545
    ee_y = 0.0007955
    ee_z = 0.62942
    ee = object(ee_x,ee_y,ee_z,"ee")
    # Add to dictionary:
    obj_dic['ee'] = ee

    # Now let's generate instruction based on the above instructions:
    generate_instruction_set(move_instruction, 'test_file1.txt')

    # ros2_command = '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "apple.urdf" --name "apple" --x 1.0 --y -2.0 --z 0.0'''

class object:
    def __init__(self, x, y, z, name):
        self.x = x
        self.y = y
        self.z = z
        self._name = name #NOTE Must match the name assigned to the object in the simulation environment

    def name(self):
        return self._name


class action_module(object):
    '''
    '''

    def initial_module(self):
        string = r"{'action': 'MoveJ', 'value': {'joint1': 0.0, 'joint2': 0.0, 'joint3': 0.0, 'joint4': 0.0, 'joint5': 0.0, 'joint6': 0.0}, 'speed': 1.0}" #Don't need a test
        return string

    def initialize_ee(self):
        # Using MoveXYZ ensures that the end-effectors rotation remains constant
        # therefore, we must initilize the ee to be in the correct orientation (ready to grasp)
        #TODO: define the initial yaw, pitch, and roll values so that the ee is pointing down
        string = r"{'action': 'MoveJ', 'value': {'joint1': -58.10, 'joint2': 25.75, 'joint3': 27.17, 'joint4': -63.59, 'joint5': -71.41, 'joint6': 77.67}, 'speed': 1.0}"
        return string

    def pre_grasp_module(self, obj):
        # Pre-grasp (0.5 (z-axis) above the object)
        string = f"{{'action': 'MoveXYZ', 'value': {{'positionx': {obj.x}, 'positiony': {obj.y}, 'positionz': {obj.z+0.1}, 'speed': 1.0}}}}"
        return string

    def move_down_module(self):
        # Grasp (this sets the values to be inside the object?)
        string = r"{'action': 'MoveL', 'value': {'movex': 0.0, 'movey': 0.0, 'movez': -0.1}, 'speed': 1.0}"
        return string
    
    def attach_module(self, obj):
        # Attach #NOTE if this fails in the simulation, perhaps the name of the endeffector is wrong as this
        # assumes that all end_effectors are called EE_egp64
        string = f"{{'action': 'Attach', 'value': {{'object': '{obj.name()}', 'endeffector': 'EE_egp64'}}}}"
        return string
    
    def move_up_module(self):
        # We need to move up after grasping to avoid collision
        string = r"{'action': 'MoveL', 'value': {'movex': 0.00, 'movey': 0.0, 'movez': 0.1}, 'speed': 1.0}"
        return string
    
    def detach_module(self,obj):
        string = f"{{'action': 'Detach', 'value': {{'object': '{obj.name()}'}}}}"
        return string
    
    def close_module(self):
        return r"{'action': 'GripperClose'}" #Don't need a test
    
    def open_module(self):
        return r"{'action': 'GripperOpen'}" #Don't need a test
    
    def above_new_position(self,x,y,z):
        string = f"{{'action': 'MoveXYZ', 'value': {{'positionx': {x}, 'positiony': {y}, 'positionz': {z+0.5}, 'speed': 1.0}}}}"
        return string
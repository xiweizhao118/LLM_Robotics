obj_dic = {}
import re
class object:
    def __init__(self, x, y, z, name):
        self.x = x*1.00
        self.y = y*1.00
        self.z = z*1.00
        self._name = name #NOTE Must match the name assigned to the object in the simulation environment

    def name(self):
        return self._name

def parse_ros2_command(command):
    # 使用更精确的正则表达式匹配参数
    params = {"name": None, "x": None, "y": None, "z": None}
    
    # 对每个参数单独匹配以确保捕获正确
    params["name"] = re.search(r"--name\s+\"?([^\"\s]+)\"?", command)
    params["x"] = re.search(r"--x\s+([0-9\.]+)", command)
    params["y"] = re.search(r"--y\s+([0-9\.]+)", command)
    params["z"] = re.search(r"--z\s+([0-9\.]+)", command)
    
    # 从正则表达式的Match对象中提取匹配值
    for key in params:
        if params[key]:
            params[key] = params[key].group(1)
            if key in ["x", "y", "z"]:  # 将数字参数转换为浮点数
                params[key] = float(params[key])

    return params

def items_setup(items_instruction):
    items = parse_ros2_command(items_instruction)
    print(items)
    item = object(items['x'],items['y'],items['z'],items['name'])
    obj_dic[items['name']] = item

    return item

if __name__ == "__main__":
    items_instruction = '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "apple.urdf" --name "apple" --x 1.0 --y 2.0 --z 0.0'''
    item = items_setup(items_instruction)
    print(obj_dic['apple'])
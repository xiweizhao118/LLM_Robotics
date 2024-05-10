
# You might print the training data to see the structure
# import json
def formatted_data():
    training_data = [
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a specific format."},
        {"role": "user", "content": "I want to place a box on the table. It is located in point (1,2,3)."},
        {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "box.urdf" --name "box" --x 1.0 --y 2.0 --z 3.0'''
        }
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "I want to place a cup on the table. It is located in point (1,2,3)."},
        {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "cup.urdf" --name "cup" --x 1.0 --y 2.0 --z 3.0'''
        }
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "I want to place a box on the table. I will also need a cup. The box is located in point (1,2,3) and the cup is located in point (4,5,6)."},
        {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "cup.urdf" --name "cup" --x 4.0 --y 5.0 --z 6.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "box.urdf" --name "box" --x 1.0 --y 2.0 --z 3.0'''
        }
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "I want to place a box on the table. I will also need a cup and a plate. The box is located in point (1,2,3), the cup is located in point (4,5,6) and the plate is located in point (7,8,9)."},
        {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "box.urdf" --name "box" --x 1.0 --y 2.0 --z 3.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "cup.urdf" --name "cup" --x 4.0 --y 5.0 --z 6.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "plate.urdf" --name "plate" --x 7.0 --y 8.0 --z 9.0'''
        }
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "I want to place a box on the table. The box's x position should be 1, y position should be 2, z position should be 3. I will also need a cup and a plate. The cup's x position should be 4, y position should be 5, z position should be 6. The plate's x position should be 7, y position should be 8, z position should be 9."},
        {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "cup.urdf" --name "cup" --x 4.0 --y 5.0 --z 6.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "box.urdf" --name "box" --x 1.0 --y 2.0 --z 3.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "plate.urdf" --name "plate" --x 7.0 --y 8.0 --z 9.0'''
        }]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "I want to place a box on the table. The box's x position should be 1, y position should be 2, z position should be 3. I will also need a cup and a plate. The cup's x position should be 4, y position should be 5, z position should be 6. The plate's x position should be 7, y position should be 8, z position should be 9. The spoon's x position should be 10, y position should be 11, z position should be 12."},
        {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "cup.urdf" --name "cup" --x 4.0 --y 5.0 --z 6.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "box.urdf" --name "box" --x 1.0 --y 2.0 --z 3.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "plate.urdf" --name "plate" --x 7.0 --y 8.0 --z 9.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "spoon.urdf" --name "spoon" --x 10.0 --y 11.0 --z 12.0'''
        }
    ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "Place a laptop at position (5, 5, 2) and a mouse at (6, 5, 1) on the table."},
            {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "laptop.urdf" --name "laptop" --x 5.0 --y 5.0 --z 2.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "mouse.urdf" --name "mouse" --x 6.0 --y 5.0 --z 1.0'''
            }
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "I need a notebook placed at (0, 0, 1) and a pen at (0, 1, 1) on my desk."},
            {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "notebook.urdf" --name "notebook" --x 0.0 --y 0.0 --z 1.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "pen.urdf" --name "pen" --x 0.0 --y 1.0 --z 1.0'''
            }
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "Can you put a flower vase at (10, 20, 3) and a book at (15, 20, 3) on the table?"},
            {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "vase.urdf" --name "flower vase" --x 10.0 --y 20.0 --z 3.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "book.urdf" --name "book" --x 15.0 --y 20.0 --z 3.0'''
            }
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "Place a bowl at (7, 4, 2), a spoon at (7, 5, 1), and a napkin at (7, 3, 1) on the table."},
            {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "bowl.urdf" --name "bowl" --x 7.0 --y 4.0 --z 2.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "spoon.urdf" --name "spoon" --x 7.0 --y 5.0 --z 1.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "napkin.urdf" --name "napkin" --x 7.0 --y 3.0 --z 1.0'''
            }
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "I need a plate placed at (3, 3, 1), a fork at (3, 4, 1), and a knife at (3, 5, 1) on the table."},
            {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "plate.urdf" --name "plate" --x 3.0 --y 3.0 --z 1.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "fork.urdf" --name "fork" --x 3.0 --y 4.0 --z 1.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "knife.urdf" --name "knife" --x 3.0 --y 5.0 --z 1.0'''
            }
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "Can you put a glass at (5, 5, 2), a bottle at (6, 5, 1), and a cup at (7, 5, 1) on the table?"},
            {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "glass.urdf" --name "glass" --x 5.0 --y 5.0 --z 2.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "bottle.urdf" --name "bottle" --x 6.0 --y 5.0 --z 1.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "cup.urdf" --name "cup" --x 7.0 --y 5.0 --z 1.0'''
            }
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "Place a chair at (10, 20, 3), a table at (15, 20, 3), and a sofa at (20, 20, 3) in the living room."},
            {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "chair.urdf" --name "chair" --x 10.0 --y 20.0 --z 3.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "table.urdf" --name "table" --x 15.0 --y 20.0 --z 3.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "sofa.urdf" --name "sofa" --x 20.0 --y 20.0 --z 3.0'''
            }
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "I need a bed placed at (3, 3, 1), a pillow at (3, 4, 1), and a blanket at (3, 5, 1) in the bedroom."},
            {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "bed.urdf" --name "bed" --x 3.0 --y 3.0 --z 1.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "pillow.urdf" --name "pillow" --x 3.0 --y 4.0 --z 1.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "blanket.urdf" --name "blanket" --x 3.0 --y 5.0 --z 1.0'''
            }]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "Can you put a chair at (5, 5, 2), a table at (6, 5, 1), and a sofa at (7, 5, 1) in the living room?"},
            {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "chair.urdf" --name "chair" --x 5.0 --y 5.0 --z 2.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "table.urdf" --name "table" --x 6.0 --y 5.0 --z 1.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "sofa.urdf" --name "sofa" --x 7.0 --y 5.0 --z 1.0'''
            }
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "Place a bed at (10, 20, 3), a pillow at (15, 20, 3), and a blanket at (20, 20, 3) in the bedroom."},
            {"role": "assistant", "content": '''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "bed.urdf" --name "bed" --x 10.0 --y 20.0 --z 3.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "pillow.urdf" --name "pillow" --x 15.0 --y 20.0 --z 3.0 @ ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "blanket.urdf" --name "blanket" --x 20.0 --y 20.0 --z 3.0'''
            }
        ]
    }
    ]
    # data = json.dumps(training_data, indent=4)
    return training_data
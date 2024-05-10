
# You might print the training data to see the structure
# import json
def formatted_data():
    training_data = [
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "I want to place a box on the table. It is located in point (1,2,3)."},
        {"role": "assistant", "content": {
            "item": "cup",
            "location": {
                "x": "1",
                "y": "2",
                "z": "3"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "I want to place a cup on the table. It is located in point (1,2,3)."},
        {"role": "assistant", "content": {
            "number": "1",
            "item": "cup",
            "location": {
                "x": "1",
                "y": "2",
                "z": "3"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "I want to place a box on the table. I will also need a cup. The box is located in point (1,2,3) and the cup is located in point (4,5,6)."},
        {"role": "assistant", "content": {
            "number": "2",
            "item": "box,cup",
            "location": {
                "box": "1,2,3",
                "cup": "4,5,6"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "I want to place a box on the table. I will also need a cup and a plate. The box is located in point (1,2,3), the cup is located in point (4,5,6) and the plate is located in point (7,8,9)."},
        {"role": "assistant", "content": {
            "number": "3",
            "item": "box,cup,plate",
            "location": {
                "box": "1,2,3",
                "cup": "4,5,6",
                "plate": "7,8,9"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "I want to place a box on the table. The box's x position should be 1, y position should be 2, z position should be 3. I will also need a cup and a plate. The cup's x position should be 4, y position should be 5, z position should be 6. The plate's x position should be 7, y position should be 8, z position should be 9."},
        {"role": "assistant", "content": {
            "number": "3",
            "item": "box,cup,plate,spoon",
            "location": {
                "box": "1,2,3",
                "cup": "4,5,6",
                "plate": "7,8,9"
            }
        }}]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "I want to place a box on the table. The box's x position should be 1, y position should be 2, z position should be 3. I will also need a cup and a plate. The cup's x position should be 4, y position should be 5, z position should be 6. The plate's x position should be 7, y position should be 8, z position should be 9. The spoon's x position should be 10, y position should be 11, z position should be 12."},
        {"role": "assistant", "content": {
            "number": "4",
            "item": "box,cup,plate,spoon",
            "location": {
                "box": "1,2,3",
                "cup": "4,5,6",
                "plate": "7,8,9",
                "spoon": "10,11,12"
            }
        }}
    ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "Place a laptop at position (5, 5, 2) and a mouse at (6, 5, 1) on the table."},
            {"role": "assistant", "content": {
                "number": "2",
                "item": "laptop,mouse",
                "location": {
                    "laptop": "5,5,2",
                    "mouse": "6,5,1"
                }
            }}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "I need a notebook placed at (0, 0, 1) and a pen at (0, 1, 1) on my desk."},
            {"role": "assistant", "content": {
                "number": "2",
                "item": "notebook,pen",
                "location": {
                    "notebook": "0,0,1",
                    "pen": "0,1,1"
                }
            }}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "Can you put a flower vase at (10, 20, 3) and a book at (15, 20, 3) on the table?"},
            {"role": "assistant", "content": {
                "number": "2",
                "item": "flower vase,book",
                "location": {
                    "flower vase": "10,20,3",
                    "book": "15,20,3"
                }
            }}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "Place a bowl at (7, 4, 2), a spoon at (7, 5, 1), and a napkin at (7, 3, 1) on the table."},
            {"role": "assistant", "content": {
                "number": "3",
                "item": "bowl,spoon,napkin",
                "location": {
                    "bowl": "7,4,2",
                    "spoon": "7,5,1",
                    "napkin": "7,3,1"
                }
            }}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "I need a plate placed at (3, 3, 1), a fork at (3, 4, 1), and a knife at (3, 5, 1) on the table."},
            {"role": "assistant", "content": {
                "number": "3",
                "item": "plate,fork,knife",
                "location": {
                    "plate": "3,3,1",
                    "fork": "3,4,1",
                    "knife": "3,5,1"
                }
            }}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "Can you put a glass at (5, 5, 2), a bottle at (6, 5, 1), and a cup at (7, 5, 1) on the table?"},
            {"role": "assistant", "content": {
                "number": "3",
                "item": "glass,bottle,cup",
                "location": {
                    "glass": "5,5,2",
                    "bottle": "6,5,1",
                    "cup": "7,5,1"
                }
            }}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "Place a chair at (10, 20, 3), a table at (15, 20, 3), and a sofa at (20, 20, 3) in the living room."},
            {"role": "assistant", "content": {
                "number": "3",
                "item": "chair,table,sofa",
                "location": {
                    "chair": "10,20,3",
                    "table": "15,20,3",
                    "sofa": "20,20,3"
                }
            }}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "I need a bed placed at (3, 3, 1), a pillow at (3, 4, 1), and a blanket at (3, 5, 1) in the bedroom."},
            {"role": "assistant", "content": {
                "number": "3",
                "item": "bed,pillow,blanket",
                "location": {
                    "bed": "3,3,1",
                    "pillow": "3,4,1",
                    "blanket": "3,5,1"
                }
            }}]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "Can you put a chair at (5, 5, 2), a table at (6, 5, 1), and a sofa at (7, 5, 1) in the living room?"},
            {"role": "assistant", "content": {
                "number": "3",
                "item": "chair,table,sofa",
                "location": {
                    "chair": "5,5,2",
                    "table": "6,5,1",
                    "sofa": "7,5,1"
                }
            }}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
            {"role": "user", "content": "Place a bed at (10, 20, 3), a pillow at (15, 20, 3), and a blanket at (20, 20, 3) in the bedroom."},
            {"role": "assistant", "content": {
                "number": "3",
                "item": "bed,pillow,blanket",
                "location": {
                    "bed": "10,20,3",
                    "pillow": "15,20,3",
                    "blanket": "20,20,3"
                }
            }}
        ]
    }
    ]
    # data = json.dumps(training_data, indent=4)
    return training_data
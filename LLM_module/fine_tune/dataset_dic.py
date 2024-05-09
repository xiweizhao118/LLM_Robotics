
# You might print the training data to see the structure
# import json
def formatted_data():
    training_data = [
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Put the cup 10 cm in front of the box"},
        {"role": "assistant", "content": {
            "what": "cup",
            "how": "move",
            "location": {
                "precise": "False",
                "position": "None",
                "relation": "box",
                "direction": "in front",
                "distance": "10 cm"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Move the pen so it's 5cm on the left of the notebook"},
        {"role": "assistant", "content": {
            "what": "pen",
            "how": "move",
            "location": {
                "precise": "False",
                "position": "None",
                "relation": "notebook",
                "direction": "left",
                "distance": "5 cm"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Lift the book and place it 10 cm behind the lamp"},
        {"role": "assistant", "content": {
            "what": "book",
            "how": "move",
            "location": {
                "precise": "False",
                "position": "None",
                "relation": "lamp",
                "direction": "behind",
                "distance": "10 cm"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Move the vase forward 10 cm"},
        {"role": "assistant", "content": {
            "what": "vase",
            "how": "move",
            "location": {
                "precise": "False",
                "position": "None",
                "relation": "None",
                "direction": "in front",
                "distance": "10 cm"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Push the salt shaker 5 cm in front of the pepper"},
        {"role": "assistant", "content": {
            "what": "salt shaker",
            "how": "move",
            "location": {
                "precise": "False",
                "position": "None",
                "relation": "pepper",
                "direction": "in front",
                "distance": "5 cm"
            }
        }}
    ]
    },
    # we can add more examples...
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Adjust the glasses to the (10,10) position on the table"},
        {"role": "assistant", "content": {
            "what": "glasses",
            "how": "move",
            "location": {
                "precise": "True",
                "position": "(10,10)",
                "relation": "None",
                "direction": "None",
                "distance": "None"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Slide the plate to a new position (10,15) on the table"},
        {"role": "assistant", "content": {
            "what": "plate",
            "how": "move",
            "location": {
                "precise": "True",
                "position": "(10,15)",
                "relation": "None",
                "direction": "None",
                "distance": "None"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Bring the fork closer to the spoon, in front of the spoon with a distance of 5 cm"},
        {"role": "assistant", "content": {
            "what": "fork",
            "how": "move",
            "location": {
                "precise": "False",
                "position": "None",
                "relation": "spoon",
                "direction": "in front",
                "distance": "5 cm"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Move the flowerpot to a new position (5,5) on the table"},
        {"role": "assistant", "content": {
            "what": "flowerpot",
            "how": "move",
            "location": {
                "precise": "True",
                "position": "(5,5)",
                "relation": "None",
                "direction": "None",
                "distance": "None"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Push the napkin holder forward past the salt shaker, with a distance of 5 cm"},
        {"role": "assistant", "content": {
            "what": "napkin holder",
            "how": "move",
            "location": {
                "precise": "False",
                "position": "None",
                "relation": "salt shaker",
                "direction": "in front",
                "distance": "5 cm"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Move the teacup three cm to the left of the saucer"},
        {"role": "assistant", "content": {
            "what": "teacup",
            "how": "move",
            "location": {
                "precise": "False",
                "position": "None",
                "relation": "saucer",
                "direction": "left",
                "distance": "3 cm"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Adjust the position of the smartphone to be directly behind the coffee mug, with a distance of 5 cm"},
        {"role": "assistant", "content": {
            "what": "smartphone",
            "how": "move",
            "location": {
                "precise": "False",
                "position": "None",
                "relation": "coffee mug",
                "direction": "behind",
                "distance": "5 cm"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Place the pencil next to the eraser on the right side, with a distance of 5 cm"},
        {"role": "assistant", "content": {
            "what": "pencil",
            "how": "move",
            "location": {
                "precise": "False",
                "position": "None",
                "relation": "eraser",
                "direction": "right",
                "distance": "5 cm"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Slide the mouse pad closer to the keyboard, with a distance of 5 cm in front of the keyboard"},
        {"role": "assistant", "content": {
            "what": "mouse pad",
            "how": "move",
            "location": {
                "precise": "False",
                "position": "None",
                "relation": "keyboard",
                "direction": "in front",
                "distance": "5 cm"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Push the remote control to the right side of the TV, with a distance of 5 cm"},
        {"role": "assistant", "content": {
            "what": "remote control",
            "how": "move",
            "location": {
                "precise": "False",
                "position": "None",
                "relation": "TV",
                "direction": "right",
                "distance": "5 cm"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Move the stapler right 5 cm"},
        {"role": "assistant", "content": {
            "what": "stapler",
            "how": "move",
            "location": {
                "precise": "False",
                "position": "None",
                "relation": "None",
                "direction": "right",
                "distance": "5 cm"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Push the tape dispenser forward 5 cm"},
        {"role": "assistant", "content": {
            "what": "tape dispenser",
            "how": "move",
            "location": {
                "precise": "False",
                "position": "None",
                "relation": "None",
                "direction": "in front",
                "distance": "5 cm"
            }
        }}
    ]
    }
    ]
    # data = json.dumps(training_data, indent=4)
    return training_data
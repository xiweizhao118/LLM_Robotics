
# You might print the training data to see the structure
# import json
def formatted_data():
    training_data = [
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Move the cup forward 10 cm relative to the box"},
        {"role": "assistant", "content": {
            "what": "cup",
            "how": "move",
            "location": {
                "precise": "False",
                "relation": "box",
                "direction": "forward",
                "distance": "10 cm"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Move the pen forward so it's beside the notebook"},
        {"role": "assistant", "content": {
            "what": "pen",
            "how": "move",
            "location": {
                "precise": "False",
                "relation": "notebook",
                "direction": "beside",
                "distance": "None"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Lift the book and place it forward of the lamp"},
        {"role": "assistant", "content": {
            "what": "book",
            "how": "move",
            "location": {
                "precise": "False",
                "relation": "lamp",
                "direction": "forward",
                "distance": "None"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Slide the vase towards the center of the table"},
        {"role": "assistant", "content": {
            "what": "vase",
            "how": "move",
            "location": {
                "precise": "False",
                "relation": "table center",
                "direction": "toward",
                "distance": "None"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Push the salt shaker forward 5 cm from the pepper"},
        {"role": "assistant", "content": {
            "what": "salt shaker",
            "how": "move",
            "location": {
                "precise": "False",
                "relation": "pepper",
                "direction": "forward",
                "distance": "5 cm"
            }
        }}
    ]
    },
    # we can add more examples...
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Adjust the glasses forward towards the edge of the table"},
        {"role": "assistant", "content": {
            "what": "glasses",
            "how": "move",
            "location": {
                "precise": "False",
                "relation": "table edge",
                "direction": "toward",
                "distance": "None"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Slide the plate to the right to align it with the cup"},
        {"role": "assistant", "content": {
            "what": "plate",
            "how": "move",
            "location": {
                "precise": "False",
                "relation": "cup",
                "direction": "right",
                "distance": "None"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Bring the fork closer to the spoon"},
        {"role": "assistant", "content": {
            "what": "fork",
            "how": "move",
            "location": {
                "precise": "False",
                "relation": "spoon",
                "direction": "closer",
                "distance": "None"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Tilt the flowerpot slightly towards the window"},
        {"role": "assistant", "content": {
            "what": "flowerpot",
            "how": "move",
            "location": {
                "precise": "False",
                "relation": "window",
                "direction": "toward",
                "distance": "slight"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Push the napkin holder forward past the salt shaker"},
        {"role": "assistant", "content": {
            "what": "napkin holder",
            "how": "move",
            "location": {
                "precise": "False",
                "relation": "salt shaker",
                "direction": "forward",
                "distance": "None"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Move the teacup three inches to the left of the saucer"},
        {"role": "assistant", "content": {
            "what": "teacup",
            "how": "move",
            "location": {
                "precise": "False",
                "relation": "saucer",
                "direction": "left",
                "distance": "three inches"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Adjust the position of the smartphone to be directly behind the coffee mug"},
        {"role": "assistant", "content": {
            "what": "smartphone",
            "how": "move",
            "location": {
                "precise": "False",
                "relation": "coffee mug",
                "direction": "behind",
                "distance": "None"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Place the pencil next to the eraser on the right side"},
        {"role": "assistant", "content": {
            "what": "pencil",
            "how": "move",
            "location": {
                "precise": "False",
                "relation": "eraser",
                "direction": "right",
                "distance": "None"
            }
        }}
    ]
    },
    {
    "messages": [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": "Slide the mouse pad closer to the keyboard"},
        {"role": "assistant", "content": {
            "what": "mouse pad",
            "how": "move",
            "location": {
                "precise": "False",
                "relation": "keyboard",
                "direction": "closer",
                "distance": "None"
            }
        }}
    ]
    }
    ]
    # data = json.dumps(training_data, indent=4)
    return training_data
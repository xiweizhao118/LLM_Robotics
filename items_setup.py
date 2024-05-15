import subprocess
import openai
# model_id = 'model-id'
input_model_id = 'input-model-id'
openai.api_key = 'api-key'

def user_place_items():
    '''
    This function is used to place items on the table
    '''
    command = []
    user_input = input("what do you want to add on the table?")  # Get user input: let's say "box" 1 2 3
    # feed the user input to our fine-tuned model
    test_messages = [
        {"role": "system", "content": "You are a robot assistant to help us extract keywords from user's demands and save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": user_input}
    ]
    completion = openai.ChatCompletion.create(
    model=input_model_id,
    messages=test_messages
    )
    gpt_reply = completion.choices[0].message
    # get the reply (dictionary format) from the model
    gpt_reply = gpt_reply['content']
    
    command.append('''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "---" --name "---" --x 0.0 --y -0.0 --z 0.0''')
    user_input = gpt_reply.split(' @ ')
    for _, cmd in enumerate(user_input):
        command.append(cmd)
    # print(command)

    # NOTE: The following code is used to run terminal commands
    for c in command:
        run_terminal_command(c)
    # return command[1:]

def run_terminal_command(command):
    '''
    This function is used to run terminal commands
    '''
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("Command output:")
        print(result.stdout)
        if result.stderr:
            print("Error message:")
            print(result.stderr)
    except Exception as e:
        print("An error occurred:", e)

# Main function
def main():
    # place items on the table
    user_place_items()
    print("Items placed on the table successfully!")


if __name__ == "__main__":
    main()  # Call the main function
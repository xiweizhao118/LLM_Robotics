import subprocess
import openai, json
from processor import processor
model_id = 'model-id-here'
input_model_id = 'input-model-id-here'
openai.api_key = 'my_openai_api_key_here'

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
    
    # user_input = user_input.split(',') #box,1,2,3 
    ## these terminal commands are better to be written in a launch file
    command.append('''ros2 run ros2_grasping spawn_object.py --package "ros2_grasping" --urdf "---" --name "---" --x 0.0 --y -0.0 --z 0.0''')
    # command.append('ros2 run ros2_grasping grasp_object.py --package "ros2_grasping" '+user_input)
    user_input = gpt_reply.split(' @ ')
    for _, cmd in enumerate(user_input):
        command.append(cmd)

    # print(command)

    # NOTE: The following code is used to run terminal commands
    # for c in command:
    #     run_terminal_command(c)
    return command[1:]


def user_language_demands():
    user_input = input("How can I help you today? ")  # Get user input
    # feed the user input to our fine-tuned model
    test_messages = [
        {"role": "system", "content": "You are a robot assistant that can extract keywords from user's demands and help us save the keywords and corresponding parameters into a dictionary format."},
        {"role": "user", "content": user_input}
    ]
    completion = openai.ChatCompletion.create(
    model=model_id,
    messages=test_messages
    )
    gpt_reply = completion.choices[0].message
    # get the reply (dictionary format) from the model
    reply_dict = json.loads(gpt_reply['content'])

    # print(reply_dict)
    return reply_dict
    
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
    items_setup_instructions_list = user_place_items()
    # Get user input and record
    move_instructions_dic = user_language_demands()
    # Process the instructions
    processor(items_setup_instructions_list, move_instructions_dic)


if __name__ == "__main__":
    main()  # Call the main function


import subprocess
import openai, json
model_id = 'model-id'
openai.api_key = 'api-key'

def user_place_items():
    '''
    This function is used to place items on the table
    '''
    user_input = input("what do you want to add on the table?")  # Get user input
    record_input("items:"+user_input)  # Record the user input, strictly in the format of "--name "box" --x 0.5 --y -0.3 --z 0.75"
    # terminal_cmd0 = f"{ros2 run ros2_grasping spawn_object.py --package \"ros2_grasping\" --urdf \"---\" --name \"---\" --x 0.0 --y -0.0 --z 0.0}"
    # terminal_cmd1 = f"{ros2 run ros2_grasping grasp_object.py --package \"ros2_grasping\" --name \"---\" --x user_input[0] --y user_input[1] --z user_input[2]}"
    # run_terminal_command(terminal_cmd0)
    # run_terminal_command(terminal_cmd1)


def user_language_demands():
    user_input = input("How can I help you today? ")  # Get user input
    record_input("commands:"+user_input)  # Record the user input
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
    reply_dict = json.loads(json.loads(gpt_reply['content']))
    #TODO: extract the keywords and corresponding parameters from the reply_dict

    
def run_terminal_command(command):
    '''
    This function is used to run terminal commands
    '''
    try:
        # 使用subprocess运行终端命令
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        # 输出命令执行的结果
        print("Command output:")
        print(result.stdout)
        # 输出命令执行的错误信息（如果有）
        if result.stderr:
            print("Error message:")
            print(result.stderr)
    except Exception as e:
        print("An error occurred:", e)

# Define a function to record user input to a file
def record_input(user_input):
    with open("user_inputs.txt", "a") as file:
        file.write(user_input + "\n")  # Write the user input to the file

# Main function
def main():
    # place items on the table
    user_place_items()
    # Get user input and record
    user_language_demands()


if __name__ == "__main__":
    main()  # Call the main function


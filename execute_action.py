import subprocess
import openai, json
model_id = 'model-id'
openai.api_key = 'open-api-key'

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
    return user_input, reply_dict["what"]

# Main function
def main():
    while True:
        user_input, item_name = user_language_demands()
        if user_input == "exit":
            break
        command = f'''ros2 run ros2_execution ros2_execution.py --ros-args -p PROGRAM_FILENAME:="{item_name}" -p ROBOT_MODEL:="irb120" -p EE_MODEL:="schunk"'''
        # run_terminal_command(command)
        print(command)
        print("Task completed successfully!")
    
    print("Goodbye!")


if __name__ == "__main__":
    main()  # Call the main function

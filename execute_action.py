import subprocess


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
    # Process the instructions
    file_name = "cube"
    # instruction = '''ros2 run ros2_execution ros2_execution.py --ros-args -p PROGRAM_FILENAME:="cube" -p ROBOT_MODEL:="irb120" -p EE_MODEL:="schunk"'''
    instruction = f'''ros2 run ros2_execution ros2_execution.py --ros-args -p PROGRAM_FILENAME:="{file_name}" -p ROBOT_MODEL:="irb120" -p EE_MODEL:="schunk"'''
    run_terminal_command(instruction)
    print("Task completed successfully!")


if __name__ == "__main__":
    main()  # Call the main function

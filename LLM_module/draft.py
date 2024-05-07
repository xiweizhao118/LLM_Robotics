import subprocess

# 定义要运行的终端命令
terminal_command = "ls -l"  # 例如，这里定义了一个简单的列出当前目录下文件的命令

def run_terminal_command(command):
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

# 在这里调用函数并传入定义的终端命令
if __name__ == "__main__":
    run_terminal_command(terminal_command)

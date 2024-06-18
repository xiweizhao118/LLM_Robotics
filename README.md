### Here is the integrated main module which generates the final action file.txt

Embedded modules:
- User place items:
  
  Record user's set-up information about items. Use fine-tuned GPT module to process it and generate ros2 commands which can be run directly in the terminal.
- User language demands:
  
  Record the user's natural language commands about item movements. Use fine-tuned GPT model to process and generate demands dictionary.
- Language demands processor:
  
  Process the demands dictionary and generate the final actions file, saved in 'test_file.txt'.

How to run?
- Open 'main.py' and type our models id and my personal openai api key. I write them in our notion workspace.
- Run 'main.py' directly and input demands as users. Finally, you will get the final actions file in the root directory.
  

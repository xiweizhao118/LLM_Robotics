__Here is the integrate main module which generates the final action file.txt__

Embedded modules:
- User place items:
  Record user's set up information about items. Use fine-tuned GPT modle to process it and generate ros2 commands which can be run directly in the terminal.
- User language demands:
  Record user's natural language commands about item movements. Use fine-tuned GPT model to process and generate demands dictionary.
- Language demands processor:
  Process the demands dictionary and generate the final actions file, saved in 'test_file.txt'.

How to run?
- Run 'main.py' directly and input demands as users. Finally you would get the final actions file in the root directionary.
  

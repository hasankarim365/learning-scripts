import os # This module allows python to interact with the Operating System

filepath = "text.txt"

if os.path.exists(filepath): # checks if the file exists
    print("File found")
    if os.path.isfile(filepath): # checks if it is a file
        print("It is a file")
    elif os.path.isdir(filepath): # checks if it is a directory
        print("It is a directory")
else:
    print("File not found") 
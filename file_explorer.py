#!/usr/bin/python3
import os
def file_explorer():
    dir_stack = []
    while True:
        print("current working directory:,", os.getcwd())
        command = input("Enter command $ ")
        if command.startswith("cd "):
            dir_stack.append(os.getcwd())
            try:
                os.chdir(command[3:])
            except FileNotFoundError:
                print("Directory not found")
                os.chdir(dir_stack.pop())
        elif command == "ls":
            print(os.listdir(os.getcwd()))
        elif command.startswith("mkdir "):
            os.mkdir(command[6:])
        elif command.startswith("rmdir "):
            os.rmdir(command[6:])
        elif command == "back":
            if dir_stack:
                os.chdir(dir_stack.pop())
            else:
                print("No previous directory")
        elif command == "exit":
            break
        else:
            print("Invalid command")

file_explorer()
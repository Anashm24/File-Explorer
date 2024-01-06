#!/usr/bin/python3
import os

def get_disk_usage(directory):
    if not os.path.exists(directory):
        print(f"Invalid command: {directory} does not exist")
        return
    try:
        total = 0
        for path, dirs, files in os.walk(directory):
            for f in files:
                fp = os.path.join(path, f)
                total += os.path.getsize(fp)
        return total
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def total_disk_usage():   
    while True:
        print("The current working directory:", os.getcwd())
        command = input("Enter the command: ")
        if command == "exit":
            break
        else:
            try:
                size = get_disk_usage(command)
                print("Total disk usage:", size)
            except Exception as e:
                print("An error occurred:", str(e))

total_disk_usage()

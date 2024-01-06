#!/usr/bin/python3
import os
import hashlib

def find_duplicates(directory):
    file_dict = {}
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            file_hash = hash_file(filepath)
            if file_hash in file_dict:
                file_dict[file_hash].append(filepath)
            else:
                file_dict[file_hash] = [filepath]

    for files in file_dict.values():
        if len(files) > 1:
            print("Duplicate files:")
            for file in files:
                print(file)

def hash_file(filepath):
    try:
        with open(filepath, 'rb') as f:
            contents = f.read()
        file_hash = hashlib.md5(contents).hexdigest()
        return file_hash
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def manage_duplicates():
    while True:
        print("Enter a command:")
        print("1. Find duplicate files")
        print("2. Exit")
        command = input("Enter command: ")

        if command == "1":
            directory = input("Enter the directory path: ")
            find_duplicates(directory)
        elif command == "2":
            break
        else:
            print("Invalid command")

manage_duplicates()

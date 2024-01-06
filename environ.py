#!/usr/bin/python3
import os

def manage_env_vars():
    while True:
        print("Enter a command:")
        print("1. Print all environment variables")
        print("2. Add a new environment variable")
        print("3. delete an environment variable")
        print("4. Verify an environment variable")
        print("5. Exit")
        command = input("enter command: ")

        if command == "1":
            print("Environment variables:")
            for key, value in os.environ.items():
                print(f"{key}: {value}")
        elif command == "2":
            key = input("Enter the name of the new environment variable: ")
            value = input("Enter the value of the new environment variable: ")
            os.environ[key] = value
            print(f"Environment variable {key} added.")
        elif command == "3":
            key = input("Enter the name of the environment variable to delete: ")
            if key in os.environ:
                del os.environ[key]
                print("Environment variable is deleted.")
            else:
                print(f"Environment variable {key} doesn't exist.")
        elif command == "4":
            key = input("Enter the name of the environment variable to verify: ")
            if key in os.environ:
                print(f"{key}: {os.environ[key]}")
            else:
                print(f"Environment variable {key} does not exist.")
        elif command == "5":
            break
        else:
            print("Invalid command")

manage_env_vars()
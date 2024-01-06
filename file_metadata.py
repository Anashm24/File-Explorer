import os
import time

def get_file_metadata(file_path):
    if not os.path.isfile(file_path):
        print("File doesn't exist")
        return

    try:
        file_info = os.stat(file_path)
        print("Size of the file: {} bytes".format(file_info.st_size))
        print("Creation time of the file: {}".format(time.ctime(file_info.st_ctime)))
        print("Last modification time of the file: {}".format(time.ctime(file_info.st_mtime)))
    except Exception as e:
        print("An error occurred:", str(e))

def file_metadata():   
    while True:
        print("The current working directory:", os.getcwd())
        command = input("Enter the command: ")
        if command == "exit":
            break
        else:
            try:
                get_file_metadata(command)
            except Exception as e:
                print("An error occurred:", str(e))

file_metadata()

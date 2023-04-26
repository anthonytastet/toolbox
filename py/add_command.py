#!/usr/bin/python3

# add command
# converts a python script in a shell binary that can be used
# without the need of prefixing "python" or appending ".py" extension to the command

from argparse import ArgumentParser
from sys import argv, exit
from os import path, chmod, stat, getenv, remove, mkdir
from shutil import copy, move
import subprocess


# [1 / 6] get path of the script to convert to a shell command
parser = ArgumentParser(description='Converts a python script to a shell binary one can use within the command line')
parser.add_argument('-f', '--file', nargs='?', help='reads path of the script to convert to a shell command')
# parser.add_argument('-f', '--file', nargs='?', help='reads path of the script to convert to a shell command')
parser.add_help=True
try:
    if len(argv) == 2:
        script_path = str(argv[1])
        if path.exists(script_path):
            SCRIPT_PATH = (script_path,) # declare it as a tuple so that the variable cannot be reassigned
        else:   
            print(f"file '{script_path}' not found")  
    else:
        while True:
            script_path =  str(input("script file path: "))
            if path.exists(script_path):
                SCRIPT_PATH = (script_path,) # declare it as a tuple so that the variable cannot be reassigned
                break
            else:   
                print(f"file '{script_path}' not found")   
except:
    print("an exception occurred [1 / 6]")
    exit("'add command' aborted.")
else:
    script = str(path.abspath(SCRIPT_PATH[0]))
    print(f"file path set to: '{script}'")
    print("--> ok.")


# [2 / 6] set permissions to rwx for the user to make the file executable
print("setting file permissions to 'executable' ...")
try:
    chmod(script, 0o700)
    # leading zeros in decimal integer literals are not permitted
    # so we use '0o' as prefix for octal integers
except:
    print("an exception occurred [2 / 6]")
    exit("'add command' aborted.")
else:
        if str(oct(stat(script).st_mode)[-3:]) == "700":
            print("--> ok.")
        else:
            print("file permissions not properly set")
    

# [3 / 6] prepend file content with a 'shebang' to set the code interpreter
def get_fileExtension(file: str):
    file_extension = ""
    extension_exists = "." in file
    if(extension_exists):
        file_extension = file.split(".", 1)[1]
    else:
        file_extension = "no-extension"
    return file_extension

script_extension = get_fileExtension(script)
print(f"script extension: '{script_extension}'")

if script_extension == "py":
    shebang = "#!/usr/bin/python3"
elif script_extension == "sh":
    shebang = "#!/bin/bash"
else:
    shebang = "#!/usr/bin/python3"

print("setting code interpreter of the file ...")
try:
    with open(script, "r+") as script:
        script.seek(0, 0)
        script_start = script.readline(len(shebang))
        script.seek(0, 0)
        script_content = script.read()
        script.seek(0, 0)
        if script_start != shebang:
            script.seek(0, 0)
            script.write(f"{shebang}{script_content}")
except:
    print("an exception occurred [3 / 6]")
    exit("'add command' aborted.")
else:
    print("--> ok.")


# [4 / 6] remove the file extension
script = str(path.abspath(SCRIPT_PATH[0]))
def get_fileBaseName(file_fullName: str):
    file_baseName = str(path.splitext(file_fullName)[0]).split("/")[-1]
    return file_baseName
print("creating command file ...")
try:
    command = get_fileBaseName(script).replace("_", "-")
    if not(path.exists(command)):
        copy(script, command)
except:
    print("an exception occurred [4 / 6]")
    exit("'add command' aborted.")
else:
    print("--> ok.")


# [5 / 6] move the binary to the user binary repository
script = str(path.abspath(SCRIPT_PATH[0]))
print("moving binary file to user binary repository ...")
try:
    command_directory = path.join(str(getenv('HOME')), "bin")
    command_baseName = get_fileBaseName(path.join(command_directory, command))
    if path.exists(command_directory):
        if not(path.exists(path.join(command_directory, command_baseName))):
            move(command, command_directory)
        else :
            print(f"command '{path.join(command_directory, command_baseName)}' already exists")
            while True:
                replace_existing = str(input(f"do you want to replace existing '{path.join(command_directory, command_baseName)}' ? (y/n): "))[0].lower().lstrip()
                if replace_existing == "y":
                    remove(path.join(command_directory, command_baseName))
                    move(command, command_directory)
                    print(f"command '{path.join(command_directory, command_baseName)}' has been replaced")
                    break
                elif replace_existing == "n":
                    print(f"original command '{path.join(command_directory, command_baseName)}' kept")
                    exit()
    else:
        mkdir(command_directory)
        move(command, command_directory)
except:
    print("an exception occurred [5 / 6]")
    exit("'add command' aborted.")
else:
    print("--> ok.")

# [6 / 6] set the binary file's permissions to executable only
print("setting binary permissions to 'read/execute' only ...")
try:
    chmod(path.join(command_directory, command_baseName), 0o555)
except:
    print("an exception occurred [6 / 6]")
    exit("'add command' aborted.")
else:
    print("--> ok.")
    print(f"new command added.")
    print(f"type '{command_baseName}' to execute.")
    subprocess.call("reload-environment")

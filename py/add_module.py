#!/usr/bin/python3

# add module
# add a custom module to a python module directory available in the PATH

from os import path, remove, chmod, stat
from sys import argv, exit
from shutil import copy
from argparse import ArgumentParser
import subprocess


# [1 / 4] get path of the module to move to the python module directory
parser = ArgumentParser(description='Adds a custom module to a python module repository available in the PATH')
parser.add_argument('-f', '--file', nargs='?', help='reads path of the python file to move to the python module repository')
try:
    if len(argv) == 2:
        module_path = str(argv[1])
        if path.exists(module_path):
            MODULE_PATH = (module_path,) # declare it as a tuple so that the variable cannot be reassigned
        else:   
            print(f"file '{module_path}' not found")  
    else:
        while True:
            module_path =  str(input("module file path: "))
            if path.exists(module_path):
                MODULE_PATH = (module_path,) # declare it as a tuple so that the variable cannot be reassigned
                break
            else:   
                print(f"file '{module_path}' not found")   
except:
    print("an exception occurred [1 / 4]")
else:
    module = str(path.abspath(MODULE_PATH[0]))
    print(f"file path set to: '{module}'")
    print("--> ok.")

# [2 / 4] set permissions to rwx for the user to allow file handling
print("setting file permissions ...")
try:
    chmod(module, 0o700)
    # leading zeros in decimal integer literals are not permitted; we use '0o' as prefix for octal integers
except:
    print("an exception occurred [2 / 4]")
    exit("'add command' aborted.")
else:
        if str(oct(stat(module).st_mode)[-3:]) == "700":
            print("--> ok.")
        else:
            print("file permissions not properly set")


# [3 / 4] move the file to the python module repository
def get_fileBaseName(file_fullName: str):
    if path.isfile(file_fullName):
        file_baseName = str(file_fullName.split("/")[-1])
    return file_baseName

module_repository = "/usr/lib/python3/dist-packages/"
module_baseName = get_fileBaseName(module)
custom_module = path.join(module_repository, module_baseName)
try:
    if path.exists(custom_module):
        print(f"module '{custom_module}' already exists")
        while True:
            replace_existing = str(input(f"do you want to replace existing '{custom_module}' ? (y/n): "))[0].lower().lstrip()
            if replace_existing == "y":
                remove(custom_module)
                copy(module, module_repository)
                print(f"module '{custom_module}' has been replaced")
                break
            elif replace_existing == "n":
                print(f"original command '{custom_module}' kept")
                exit()
    else:
        copy(module, module_repository)
except:
    print("an exception occurred [3 / 4]")
    exit("'add module' aborted.")
else:
    print("--> ok.")

# [4 / 4] set the module's permissions to read only
print("setting module permissions to 'read/execute only' ...")
try:
    chmod(path.join(module_repository, module_baseName), 0o555)
except:
    print("an exception occurred [4 / 4]")
    exit("'add module' aborted.")
else:
    print("--> ok.")
    print(f"custom module added in '{module_repository}'.")
    print(f"type 'import {module_baseName}' in a python script to use it.")
    subprocess.call("reload-environment")

#!/usr/bin/python3

# sort files
# sort current directory files into new directories created after their extension name

from custom_module import get_childItems, get_fileExtension, clean_fileName, get_fileBaseName
from os import path, mkdir
from shutil import move
from argparse import ArgumentParser
import subprocess

parser = ArgumentParser(description='Sort files in the specified directory')
parser.add_argument('path',
                    nargs='?',
                    help='read path of the directory',
)
parser.add_argument('-s',
                    '--separator',
                    choices=['-', '_'],
                    help='choose between a hypen and an underscore as a word separator in file names'
)
parser.add_argument('-m',
                    '--move',
                    help='move files into directories created after their extension name',
                    action='store_true'
)
args = parser.parse_args()

# [1/2] get path of the directory to sort
try:
    if args.path:
        directory_path = str(args.path)
        if path.exists(directory_path):
            DIRECTORY_PATH = (directory_path,) # declare it as a tuple so that the variable cannot be reassigned
        else:   
            print(f"directory '{directory_path}' not found")  
    else:
        while True:
            directory_path =  str(input("directory file path: "))
            if path.exists(directory_path):
                DIRECTORY_PATH = (directory_path,) # declare it as a tuple so that the variable cannot be reassigned
                break
            else:   
                print(f"directory '{directory_path}' not found")   
except:
    print("an exception occurred [1/2]")
    exit("'add command' aborted.")
else:
    target_directory = str(path.abspath(DIRECTORY_PATH[0]))
    files_list = get_childItems(target_directory)
    print(f"directory path set to: '{target_directory}'")
    print("--> ok.")


if args.separator:
    word_separator=args.separator
else:
    word_separator="_"

# [2/2]
if args.move:
    try:
        for file in files_list:

            file_extension = get_fileExtension(file)

            sub_directory = path.join(target_directory, file_extension)
            sub_directoryBaseName = get_fileBaseName(sub_directory)

            parent_directory = "/".join(sub_directory.split("/",)[:-1])
            parent_directoryBaseName = get_fileBaseName(parent_directory)

            file_name = path.join(target_directory, file)
            file_nameBaseName = get_fileBaseName(file_name)
            
            file_nameCleaned = path.join(target_directory, clean_fileName(file, word_separator))
            file_nameCleanedBaseName = get_fileBaseName(file_nameCleaned)

            # rename items
            move(file_name, file_nameCleaned)
            if file_nameCleanedBaseName != file_nameBaseName:
                print(f"renamed: '{file_nameBaseName}' --> '{file_nameCleanedBaseName}'")

            # sort items
            if path.isfile(file_nameCleaned):
                if path.exists(sub_directory):
                    if not path.exists(path.join(sub_directory, file_nameCleanedBaseName)):
                        move(file_nameCleaned, sub_directory)
                        if file_nameCleaned != path.join(sub_directory, file_nameCleanedBaseName):
                            print(f"moved: '{file_nameCleanedBaseName}' --> '{sub_directory}'")
                    else:
                        print(f"a file '{file_nameCleanedBaseName}' already exists in {sub_directory}")
                else:
                    if not sub_directoryBaseName in parent_directory:
                        mkdir(sub_directory)
                        if not path.exists(path.join(sub_directory, file_nameCleanedBaseName)):
                            move(file_nameCleaned, sub_directory)
                            if file_nameCleaned != path.join(sub_directory, file_nameCleanedBaseName):
                                print(f"moved: '{file_nameCleanedBaseName}' --> '{sub_directory}'")
                        else:
                            print(f"a file '{file_nameCleanedBaseName}' already exists in {sub_directory}")
    except:
        print("an exception occurred [2/2]")
    else:
        print("files sorted.")
        subprocess.call("reload-environment")
else:
    try:
        for file in files_list:

            file_extension = get_fileExtension(file)

            sub_directory = path.join(target_directory, file_extension)
            sub_directoryBaseName = get_fileBaseName(sub_directory)

            parent_directory = "/".join(sub_directory.split("/",)[:-1])
            parent_directoryBaseName = get_fileBaseName(parent_directory)

            file_name = path.join(target_directory, file)
            file_nameBaseName = get_fileBaseName(file_name)

            file_nameCleaned = path.join(target_directory, clean_fileName(file, word_separator))
            file_nameCleanedBaseName = get_fileBaseName(file_nameCleaned)

            # rename items
            move(file_name, file_nameCleaned)
            if file_nameCleanedBaseName != file_nameBaseName:
                print(f"renamed: '{file_nameBaseName}' --> '{file_nameCleanedBaseName}'")
    except:
        print("an exception occurred [2/2]")
    else:
        print("files sorted.")
        subprocess.call("reload-environment")

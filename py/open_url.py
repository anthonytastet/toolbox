#!/usr/bin/python3
# open url
# open an url (writen in a file) with a browser (ex: firefox)

from argparse import ArgumentParser
from sys import argv
from os import path
import subprocess

# [1/2] get path of the file containing the url
parser = ArgumentParser(description='Reads a file and open the first url found')
parser.add_argument('-f', '--file', nargs='?', help='reads path of the file containing the url')
parser.add_help=True
try:
    if len(argv) == 2:
        file_path = str(argv[1])
        if path.exists(file_path):
            FILE_PATH = (file_path,) # declare it as a tuple so that the variable cannot be reassigned
        else:   
            print(f"file '{file_path}' not found")  
    else:
        while True:
            file_path =  str(input("file path: "))
            if path.exists(file_path):
                FILE_PATH = (file_path,) # declare it as a tuple so that the variable cannot be reassigned
                break
            else:   
                print(f"file '{file_path}' not found")   
except:
    print("an exception occurred [1/2]")
    exit("'open url' aborted.")
else:
    file = str(path.abspath(FILE_PATH[0]))
    print(f"file path set to: '{file}'")
    print("--> ok.")

# [2/2] readfile and open url
print("reading file content ...")
try:
    with open(file, "r+") as file:
        file.seek(0, 0)
        url = file.readline()
        open_url = subprocess.Popen(["firefox", url])
except:
    print("an exception occurred [2/2]")
    exit("'open url' aborted.")
else:
    print("--> ok.")
    print("url opened.")
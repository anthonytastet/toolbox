#!/usr/bin/python3
# get colors
# get color palette of a specified image

from custom_module import get_childItems
from colorthief import ColorThief
# import matplotlib.pyplot as plot
import colorsys
from sys import argv
from os import path
from argparse import ArgumentParser

# [ 1/3] get path of the image
parser = ArgumentParser(description='get color palette of a specified image')
parser.add_argument('-p', '--path', nargs='?', help='reads path of the image')
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
    print("an exception occurred [ 1/3]")
    exit("'get colors' aborted.")
else:
    get_colors = ColorThief(file_path)
    print(f"file path set to: '{file_path}'")
    print("--> ok.")

# [ 2/3] get palette size
try:
    while True:
        palette_size = int(input("palette size: "))
        break
except:
    print("an exception occurred [ 2/3]")
    exit("'get colors' aborted.")
else:
    color_palette = get_colors.get_palette(color_count=palette_size) 
    # plot.imshow([[color_palette[i] for i in range(palette_size)]])
    # plot.show()
    print(f"palette size set to: '{palette_size}'")
    print("--> ok.")

# [ 3/3] extract palette from image
try:
    color_index=0
    for color in color_palette:
        print("\n")
        color_index+=1
        print(f"--> palette [{color_index}/{palette_size}]")
        print(f"hex: # {color[0]:02x}{color[1]:02x}{color[2]:02x}")
        print(f"rgb: {color}")
        print(f"hsv: {colorsys.rgb_to_hsv(*color)}")
        print(f"hls: {colorsys.rgb_to_hls(*color)}")
except:
    print("an exception occurred [ 3/3]")
    exit("'get colors' aborted.")
else:
    print("\n")
    print("color palette extracted.")

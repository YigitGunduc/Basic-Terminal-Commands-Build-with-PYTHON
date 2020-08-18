#!/c/Users/gunduc/anaconda3/python

import os
from sys import argv

dirName = argv[1]

def main(dir):
    try:
        os.mkdir(dir)
        print("Directory " , dir ,  " Created ") 
    except FileExistsError:
        print("Directory " , dir ,  " already exists")        
main(dirName)
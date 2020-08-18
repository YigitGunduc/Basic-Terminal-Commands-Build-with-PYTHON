#!/c/Users/gunduc/anaconda3/python
import os
from sys import argv

pros = argv[1]
dirName = argv[2]

def main(pro,dir):
    if pro == "m":
        try:
            os.mkdir(dir)
            print("Directory " , dir ,  " Created ") 
        except FileExistsError:
            print("Directory " , dir ,  " already exists")  
    elif pro == "r":
        try:   
            if os.path.exists(dir):
                os.remove(dir)
            else:
                print("The file does not exist")
        except PermissionError:
            print("Permission Denied")
    else:
        print("command not found")
wa w
main(pros,dirName)



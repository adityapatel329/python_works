import os
from pathlib import Path
path = "C:\\Users\\aditya.patel\\Documents"

name = input("Enter the folder name : ")
ext1 = input("Enter the first extension name to be search : ")
ext2 = input("Enter the second extension name that has to be changed : ")

full_path = os.path.join(path,name)

for root,dirs,file in os.walk(full_path):
    for file_name in file:
        file_path = os.path.join(root,file_name)
        if '.txt' in file_path:
            newfile = file_path.replace(ext1,ext2)
            os.rename(file_path,newfile)

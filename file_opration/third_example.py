import os
import shutil

path = 'C:\\Users\\aditya.patel\\Documents'

name = input("Enter a directory name : ")
new_folder = input("Enter another file name : ")

full_path = os.path.join(path,name)

new_folder_path = os.path.join(path,new_folder)
print(new_folder_path)
os.makedirs(new_folder_path)


for root,dirs,file in os.walk(full_path):
    for file_name in file:
        file_path = os.path.join(root,file_name)
        s = shutil.copy(file_path,new_folder_path)
        print(s)

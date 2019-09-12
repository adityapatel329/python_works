import os
import re
path = 'C:\\Users\\Public\\Downloads\\aditya-works\\Assigment_10_11-Sep-2019'
name = input("Enter the folder name : ")
ext = input("Enter the Second Folder Name : ")
full_path = os.path.join(path,name)
l = []
d = []

for root,dirs,file in os.walk(full_path):
    for dir_name in dirs:
        d.append(os.path.join(root,dir_name))
        #print(dir_path)
    for file_name in file:
        l.append(os.path.join(root,file_name))

print(l)
print(d)
new_folder = os.makedirs(ext)
for root,dirs,file in os.walk(new_folder):
    for dir_name in d:
        os.makedirs(dir_name)
    for file_name in l:
        os.makedirs(file_name)
#for root,dirs,file in os.walk()

#for i in l:


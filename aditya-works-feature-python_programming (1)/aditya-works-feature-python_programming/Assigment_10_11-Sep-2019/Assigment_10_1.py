import os
import re
path = 'C:\\Users\\Public\\Downloads\\aditya-works\\Assigment_10_11-Sep-2019'
name = input("Enter the folder name : ")
ext = input("Enter the extension name : ")
full_path = os.path.join(path,name)
l = []
d = []

for root,dirs,file in os.walk(full_path):
    for file_name in file:
        pattern = '[a-z].txt'
        ten = re.findall(pattern,file_name)
        l.append(ten)
print(l)
#for i in l:




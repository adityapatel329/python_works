from sys import *
import os
path = os.path.join('C:\\Users\\Public\\Downloads\\aditya-works\\Assigment_9_20-Aug-2019\\Assigment_9_3\\datafiles')
name = argv[1]
with open(name,'w') as f:
    f1 = open("C://Users//Public//Downloads//aditya-works//Assigment_9_20-Aug-2019//input_file.txt")
    for i in f1.read():
        f.write(i)
    


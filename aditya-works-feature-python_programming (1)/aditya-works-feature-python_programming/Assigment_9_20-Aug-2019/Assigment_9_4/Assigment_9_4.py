from sys import *
import os
path = os.path.join('C://Users//Public//Downloads//aditya-works//Assigment_9_20-Aug-2019')
name = argv[1]
name2 = argv[2]

f1 = open("C:\\Users\\Public\\Downloads\\aditya-works\\Assigment_9_20-Aug-2019\\Assigment_9_4\\datafiles\\input_file.txt")
f2 = open("C:\\Users\\Public\\Downloads\\aditya-works\\Assigment_9_20-Aug-2019\\Assigment_9_4\\datafiles\\test.txt")
if f1.read() == f2.read():
    print("Content same")
else:
    print("Conent Different")



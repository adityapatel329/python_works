from sys import *
import os
path = os.path.join("C:\\Users\\Public\\Downloads\\aditya-works\\Assigment_9_20-Aug-2019\\Assigment_9_5\\datafiles")
name = argv[1]
string = argv[2]

with open('C:\\Users\\Public\\Downloads\\aditya-works\\Assigment_9_20-Aug-2019\\Assigment_9_5\\datafiles\\test.txt','r') as f:
    p = f.readlines()
    print("Occurence",p.count('mars'))
#print(name)
#print("File not exits")
        

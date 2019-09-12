from sys import argv
import os
path = os.path.join("C:\\Users\\Public\\Downloads\\aditya-works\\Assigment_9_20-Aug-2019\\Assigment_9_2\\datafiles")

name = argv[1]

f = open('C:\\Users\\Public\\Downloads\\aditya-works\\Assigment_9_20-Aug-2019\\Assigment_9_2\\datafiles\\test.txt','r')
print(f.read())


import os
from sys import *
p = os.getcwd()
d = argv[1]
if d not in p:
	print("File not exists : ")
else:
	print("File exists")

import os

path = "C:\\Users\\aditya.patel\\Documents\\Demo"

for root,dir,file in os.walk(path):
    for file_name in file:
        if file_name.endswith('.txt'):
            print(file_name)
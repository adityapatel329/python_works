import os
from get_arguments import *

if __name__ == "__main__":
    def read():
        f=open(args.filename,'r')
        print(f.read())
        f.close()
    def write():
        f=open(args.filename,'w')
        f.write(args.writing)
        print("Successfully written")
        f.close()
    def nlines():
        f=open(args.filename)
        print("1. FirstLine")
        print("2. LastLine")
        choice=int(input("Enter which line to find"))
        if choice == 1:
            print(f.readline())
        elif choice == 2:
            lines=f.read().splitlines()
            last_lines=lines[-1]
            print(last_lines)
        f.close()

    def copy():
        f=open(args.filename)
        f1=open(args.outputname,'w')
        f1.write(f.read())
        f.close()
        f1.close()
        print("Data copied succesfully")
    def file_display():
        for f in os.listdir():
            file_name ,file_ext = os.path.splitext(f)
            print(file_name,file_ext)

    def re_name():
        file_display()
        choice=input("choice which file to be renamed : ")
        new_name=input("Type a new name : ")
        os.rename(choice,new_name)
        print("\nrename successfully\n")
        file_display()

    def delete_file():
        file_display()
        choice=str(input("Choice a file to be deleted : "))
        print("Delete successfully")
        os.remove(choice)

        
    if args.operation == "read":
        read()
    
    if args.operation == "write":
        write()
        
    if args.operation == 'nlines':
        nlines()

    if args.operation == 'copy':
        copy()

    if args.operation == 're_name':
        re_name()
        
    if args.operation == 'delete_file':
        delete_file()
        
    if args.operation == 'display':
        file_display()

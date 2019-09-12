from get_arguments import *

if __name__ == "__main__":
    n1=args.number1
    n2=args.number2
    
    def add(n1,n2):
        print(n1+n2)
    
    def sub(n1,n2):
        print(n1-n2)
        
    def mul(n1,n2):
        print(n1*n2)
        
    if args.operation == "add":
        add(n1,n2)
        
    elif args.operation == "sub":
        sub(n1,n2)
        
    elif args.operation == "mul":
        mul(n1,n2)

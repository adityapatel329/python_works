class Demo:
    value = 121
    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2

    def fun(self):
        print("Instance variable : ",self.no1)

    def gun(self):
        print("Instance variable  : ",self.no2)

if __name__ == "__main__":
    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter second number : "))
    obj1 = Demo(n1,n2)
    n3 = int(input("Enter third number : "))
    n4 = int(input("Enter fourth numvber : "))
    obj2 = Demo(n3,n4)
    
    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()
    print("Class variable : ",obj2.value)

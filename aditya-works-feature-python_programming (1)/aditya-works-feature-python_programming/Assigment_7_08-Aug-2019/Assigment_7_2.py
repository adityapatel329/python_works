class BankAccount:
    roi = 10.5
    def __init__(self,name,amount=0):
        self.name = name
        self.amount = amount

    def deposit(self):
        mount = int(input("Enter your amount for desposit : "))
        self.amount = self.amount + mount

    def withdraw(self):
        withdr = int(input("Enter you amount for withdraw : "))
        self.amount = self.amount - withdr

    def calculateintrest(self):
        calculateintrest = ((self.amount * self.roi * 10.5)/100)
        print("Interst : ",calculateintrest)
        
    def display(self):
        print("Name : ",self.name)
        print("Amount : ",self.amount)


if __name__ == "__main__":

    name = input("Enter your name : ")
    amount = int(input("Enter your starting amount : "))
    obj1 = BankAccount(name,amount)
    obj1.deposit()
    obj1.withdraw()
    obj1.calculateintrest()
    obj1.display()
    name1 = input("Enter your name : ")
    amount1 = int(input("Enter your starting amount : "))
    obj2 = BankAccount(name,amount)
    obj2.deposit()
    obj2.withdraw()
    obj2.calculateintrest()
    obj2.display()


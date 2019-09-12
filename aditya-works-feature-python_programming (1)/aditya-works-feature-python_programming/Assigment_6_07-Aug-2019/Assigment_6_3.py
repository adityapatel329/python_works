class Arithmetic:
    def __init__(self,value1=0.0,value2=0.0,value3=0.0):

        self.value1 = value1
        self.value2 = value2
        self.value3 = value3

    def accept(self):
        self.value1 = int(input("Enter value one : "))
        self.value2 = int(input("Enter value Two : "))
        #self.value3 = int(input("Enter value Three : "))

    def addition(self):
        self.value3 = self.value1 + self.value2
        return self.value3

    def subtraction(self):
        self.value3 = self.value1 - self.value2
        return self.value3

    def multiplication(self):
        self.value3 = self.value1 * self.value2 
        return self.value3

    def division(self):
        self.value3 = self.value1 / self.value2
        return self.value3

if __name__ == "__main__":
    obj1 = Arithmetic()
    obj2 = Arithmetic() 
    obj1.accept()
    print("Addition : ",obj1.addition())
    print("Subtraction : ",obj1.subtraction())
    print("Multiplication : ",obj1.multiplication())
    print("Division : ",obj1.division())
    obj2.accept()
    print("Addition : ",obj2.addition())
    print("Subtraction : ",obj2.subtraction())
    print("Multiplication : ",obj2.multiplication())
    print("Division : ",obj2.division())
    

    

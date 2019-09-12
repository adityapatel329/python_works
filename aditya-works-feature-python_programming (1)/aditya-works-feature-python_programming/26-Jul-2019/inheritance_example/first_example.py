class Person:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

    def isEmployee(self):
        return False

class Emplyoee(Person):

    def isEmployee(self):
        return True

emp = Person("Aditya")
print(emp.getname(), emp.isEmployee())

emp = Emplyoee("Shubham")
print(emp.getname(),emp.isEmployee())

from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod 
    def display(self):
        None

class B(A):
    def display(self):
        print("This is display method")

obj = B() # we can creeate object of abstract class
obj.display()

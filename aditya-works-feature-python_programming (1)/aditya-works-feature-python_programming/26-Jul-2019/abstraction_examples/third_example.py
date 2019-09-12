from abc import ABC,abstractmethod

class X(ABC):

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class Y(X):
    def m1(self):
        print("This is M1")

class Z(Y):
    def m2(self):
        print("This is M2")


obj = Z()
obj.m1()
obj.m2()


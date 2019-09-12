from abc import ABC,abstractmethod

class Cal(ABC):
    def __init__(self,value,sec):
        self.value = value
        self.sec = sec
    @abstractmethod
    def add(self):
        pass
    
    @abstractmethod
    def sub(self):
        pass

class C(Cal):
    def add(self):
        print(self.value + self.sec)
    def sub(self):
        print(self.value - self.sec)

obj = C(100,100)
obj.add()
obj.sub()

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):
    def eat(self):
        print("Eat non-veg")

class Cow(Animal):
    def eat(self):
        print("Eat veg")

t = Tiger()
t.eat()

c = Cow()
c.eat()

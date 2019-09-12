class Dog:
    species = 'mammal'

    def __init__(self,name,age):
        self.name = name
        self.age = age

philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

print("{} is {} years old and {} is {} years old. ".format(philo.name, philo.age, mikey.name, mikey.age))

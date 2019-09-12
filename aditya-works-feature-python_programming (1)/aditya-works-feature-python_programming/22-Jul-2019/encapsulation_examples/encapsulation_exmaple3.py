clas Person n:
    def __init__(self):
        self.name = 'Majula'
        self.__lastname = 'Dube'

    def PrintName(self):
        return self.name + '' + self.__lastname

P = Person()

print(P.name)
print(P.PrintName())
print(P.__lastname)

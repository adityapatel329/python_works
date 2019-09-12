class Compute:

    def area(self ,x = None, y = None):

        if x != None and y != None:
            return x * y

        elif x != None:
            return x * x

        else:
            return 0

obj = Compute()

print("Area : ",obj.area())
print("Area : ",obj.area(2))
print("Area : ",obj.area(4, 5))

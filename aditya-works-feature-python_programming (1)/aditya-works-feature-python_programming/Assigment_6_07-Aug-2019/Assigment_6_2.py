class Circle:
    pi = 3.14
    def __init__(self,radius= 0.0,area=0.0,circumference=0.0):
        self.radius = radius
        self.area = area
        self.circumference = circumference
        

    def accept(self):
        self.radius = int(input("Enter your radius : "))
    def calculatearea(self):
        self.area =self.radius *self.radius *self.pi

    def calculatecircumferencce(self):
        self.circumference = 2 *self.pi *self.radius

    def display(self):
        print("Radius : ",self.radius)
        print("Area : ",self.area)
        print("Circumference : ",self.circumference)

if __name__ == "__main__":
    
    obj1 = Circle()
    obj2 = Circle()
    obj1.accept()
    obj1.calculatearea()
    obj1.calculatecircumferencce()
    obj1.display()
    obj2.accept()
    obj2.calculatearea()
    obj2.calculatecircumferencce()
    obj2.display()
    

    

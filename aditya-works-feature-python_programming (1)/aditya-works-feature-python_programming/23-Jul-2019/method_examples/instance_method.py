class DecoratorExample:
    def __init__(self):
        print("Hello World !")
        self.name = 'Decorator_Exmaple'

    def example_function(self):
        print("I am an instance method !")
        print('My name is ',self.name)

de = DecoratorExample()
de.example_function()

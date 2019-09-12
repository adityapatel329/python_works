class DecoratorExample:
    def __init__(self):
        print('Hello, world')

    @classmethod
    def example_function(cls):
        print("In a class method ")
        cls.some_other_function()

    @staticmethod
    def some_other_function():
        print('Hello')

de = DecoratorExample()

de.example_function()

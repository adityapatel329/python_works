## Inner Classes in Python
* You have probably heard of the nested functions in Python.
* Inner or Nested Class is defined inside another class.
```
## outer class
class Outer:
    ## inner class 
    class Inner:
        pass
        
        ## multilevel inner class
        class InnerInner:
            pass
    ## another inner class
    class _Inner:
      
    pass
        
        
```
## Why Inner Classes : 
1. Grouping of two or more classes.Suppose you have two classes 
Car and Engine.
Every Car needs an Engine.But, Engine won't be used without a Car.
So, you make the Engine an inner class to the Car.It helps save code.
2. Hiding code is another use of Nested classes. You can hide the 
Nested classes from the outside world.
3. It's easy to understand the classes. Classes are closely related here.
You don't have to search for the classes in the code. They are all together.

# Coding Inner Class
* Implementing the inner or nested classes is not difficult.
* You can access the inner class in the outer class using the self keyword.
* So you can perform operation in the outer class.
* You can't however access the outer class in an inner class.

## Multiple Inner Classes
* It is a class containing more than one inner class. You can have more than
one inner class in a class. As we defined earlier, it's easy to implement 
multiple inner classes.
## Multilevel Inner Classes
* In multilevel inner classes, the inner class contains another 
class which inner classes to the previous one.
* You can see the structure of this hierarchy 
## Self in Python
* Self represent the instance of the class.
* By using the "self" keyword we can access the attributes with the 
given arguments.
* The reason you need to use self. is because Python does
not use the @ syntax to refer to instance attribute.
* Python decided to do method in a way that makes the instance
to which the method belong be passed automatically, but not received automatically
* The first parameter of methods is the instance the method is called on
* Self is a convention and not a real python keyword self is parameter in function
and user can user another parameter name in place of it.
* But it is advisable to use self because it increase the readability of code.
## Object Creation 
* Objects are most useful when we also need to keep some that is updated from 
time.
* Consider a turtle object. Its state consists of things like its position,
its heading, its color, and its shape.
* A method like left(90) updates the turtle heading, forward changes its position
and so on.
* For a bank account object, a main component of the state would be the current balance,
and perhaps a log of all transactions.
* This method would allow us to query the current balance, deposit new funds,
or make a payment.

Object definition : A compound data type that is often used to model a thing
or concept in the real world. It bundles together the data and the operations 
that are relevant for that kind of data. Instance and object are used interchangeably.
```
class dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def display(self):
        print("Name of dog : ",self.name)
        print("Color of dog : ",self.dog)
d = dog("rocky","brown")
d.display()
```
Output:
```
Name of dog : rocky
Color of dog : brown
```
* In above code d is a object of class dog and using this "d" object 
we can call methods inside the class.
## Python Constructor
* A constructor is a special type of method which is used to initialize the 
instance member of the class.
Constructor can be of two types.
1. Parameterized Constructor
2. Non-Parameterized Constructor 
* Constructor definition is executed when we create the object of this class.
* Constructors also verify that there are enough resources for the object to 
perform any start-up task.
## Creating the constructor in python
* In python, the method __init__ simulates the constructor of the class.
* This method is called when the class is instantiated.
* We can pass any number of arguments at the time of creating 
the class object, depending upon __init__ definition.
* It is mostly used to initialize the class attributes. Every class must have
a constructor,even if it simply relies on the default constructor.

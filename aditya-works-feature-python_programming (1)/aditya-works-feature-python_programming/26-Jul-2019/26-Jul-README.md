## Data Abstraction 
* As we consider the wide set of things in the world we would like to represent
in our programs, we find that most of them have compound structure.
* For example, we would like our programming language to have the capacity to couple
together a latitude and longitude to form a pair, a compound data value that
our programs can manipulate as a single conceptual unit, but which also has two 
parts that can be considered individually.
* The use of compound data enables us to increase the modularity of our 
programs.
* if we can manipulate geographic positions as whole values, then 
we can shield parts of our program that compute using positions from the 
details of how those positions are represented.
* The general technique of isolating the parts of a program
that deal with how data are represented from the parts that deal
with how data are manipulated is a powerful design methodology 
called data abstraction.
* Data abstraction is similar in character to functional abstraction.
## Abstract Class
* Abstract classes are classes that contain one or more
abstract methods.
* An abstract method is a method that is declared, but contains no implementation.
* Abstract classes cannot not be instantiated, and require subclasses to provide
implementations for the abstract methods.
* Subclasses of an abstract class in Python are not required to implement 
abstract methods of the parent class.
## Polymoorpshim 
* The word polymorphism means having many form.
* In programming, polymorphism means same function name
being uses for different types.
```
# in-built polmorphic functions
print(len("geeks"))
print(len([10, 20, 30]))
```
Output:
```
5
3
```
### Polymorphism with class methods:
* Polymorphism is an important feature of class definition in Python that is 
utilized when you have commonly named method across or subclasses.
* This allows functions to use objects of any of these polymorphic classes 
without needing to be aware of distinctions across the classes.
* Polymorphism can be carried out through inheritance with subclasses making use
of base class method or overriding them.
* To make use of polymorphism, we're going to create two distinct classes to use 
with two distinct objects. 
* Each of these distinct classes need to have an interface that is in common 
so that they can be used polymorphically, so we will give them methods 
that are distinct but that have the same name.
* We will create a Shark class and a Clownfish class, each which will define
methods for swim(), swim_backwards() and skeleton().

### Polymorphism with a function
* We can also create a function that can take any object allowing for polymorphism.
* Let's create a function called in_the_pacific() which takes in an object we can all fish.
* Though we are using the name fish, any instantiated object will be able to be called into this functions.
```
def in_the_pacific(fish)
```
Next we'll give the function something to do that uses the fish object we passed to it.
In this case we'll call the swim() methods, each of which is defined in the two classes Shark and 
Clownfish.
```
def in_the_pacific(fish):
fish.swim()
```
Next we'll create instantiations of both Shark and Clownfish classes if we don't
have them already. With those,we can call their action using the same in_the_pacific() function:
```
def in_the_pacific(fish):
    fish.swim()
sammy = Shark()
casey = Clownfish()

in_the_pacific(sammy)
in_the_pacific(casey)
```
Output:
```
The shark is swimming 
The clownfish is swimming.
```
## Python Inheritance
* Inheritance enables us to define a class that takes all the functionality
from parent class and allow us to add more.
* Inheritance :- 
It refers to defining a new class with little or no modification
to an existing class. The new class is called derived class and the one
from which it inherits is called the base class.

Python Inheritance Syntax
```
class BaseClass:
    Body of base class
class DerivedClass(BaseClass):
    Body of derived class
```
Derived class inherits features from the base class, adding a new features 
to it. This results into re-usability of code.
## Different form of inheritance
1. Single Inheritance : When a child classes inherits form only one
parent class, it is called as single inheritance.

2. Multiple Inheritance : When a child class inherits from 
multiple parent classes it is called as multiple inheritance.

3. Multilevel inheritance : When we have child and grand child relationship.
4. Hierarchical inheritance More than one derived classes are created from a single base.
5. Hybrid inheritance: This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.
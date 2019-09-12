## What is Object-Oriented Programming(OOP)?
* Object-oriented Programming,or OOP for short, is a programming paradigm
which provides a means of structuring programs sp that properties and behaviors 
are bundled into individual objects.
* For instance,an object could represent a person with a name property
,age,address,etc., with behaviors like walking,talking,breathing, and running.
* Email with properties like recipient list,subject,body,etc.
and behaviors like adding attachments and sending.
* Another common programming paradigm is procedural programming which
structures a program like a recipe in that it provides a set of steps,in the 
form of function and code blocks,which flow sequentially in order to complete
a task.
## Classes in Python
* Focusing first on the data, each thing or object is an instance of some class.
* The primitive data structure available in Python,like numbers,strings, and lists
are designed to represent simple things like the cost of something,the name of a person
and your favorite colors,respectively.
* What if you wanted to represent something much more complicated ?
* For example, lets say you wanted to track a number of different animals.
* if you used a list,the first element could be the animal's name while the second element could 
represent its age.
* How would you know which element is supposed to be which ?
* What if you had 100 different animals ?
* Are you certain each animal has both a name and an age, and so
forth?
* What if you wanted to add other properties to these animals?
* This lacks organization, and it's the exact need for classes.
* Classes are used to create new user-defined data structures that contain 
arbitrary information about something.
* In the case of an animal,we could crate an Animal() class to track
properties about the Animal like the name and age.
* It's important to note that a class just provides structure- it's a blueprint for 
how something should be defined, but it doesn't actually provide any real content itself.
* The Animal() class may specify that the name and age are necessary for defining
an animal, but it will not actually state what a specific animal's name or age is.
## Python Objects (Instances)
* While the class is the blueprint,an instance is a copy of the class with actual values,
literally an object belonging to a specific class.
* It's not an idea anymore; it's an actual animal,like a dog named Roger who's eight years old.
* Put another way, a class is like a form a questionnaire.
* It defines the needed information.
* After you fill out the form, your specific copy is an instance of the class;
it contains actual information relevant to you.

## Defining a Class in Python
```
class Dog:
    pass
```
* You start with the class keyword to indicate that you are creating a class,
then you add the name of the class
* Also, we used the Python keyword pass here.This is very often used as a place 
holder where code will eventually go.it allows us to run this code without throwing an error.
```
class Dog(object):
    pass
```
The(object) part in parentheses specifies the parent class that you are inherting
from

## Instance Attributes 
* All classes create objects, and all objects contain characteristics called attributes 
* Use the __init__() method to initialize and object's initial attributes by giving them their default value 
* This method must have a least one arguments as well as the self variable,
which refers to te object itself
```
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
* In the case of out Dog() class, each dog has specific name and age,
which is obviously important to know for when you start actually creating
different dogs.
* Remember : the class is just for defining the Dog, not actually creating instances if 
individual dogs with specific names and ages;
* Similarly the self variable is also an instance of the class.
* Since instances of a class have varying we could state Dog.name = name
rather than self.name = name.
* But since not all dogs share the same name, we need to be able to assign 
different values to different instances.
## Class Attributes 
* While instance attributes are specific to each object,class attributes are the same
for all instances -  which in the case is all dogs.
```
class Dog:
    species = 'mammal'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
 print(Dog())
 print(Dog())
 a = Dog()
 b = Dog()
 print(a == b)
```
Output:
```
<__main__.Dog object at 0x1004ccc50>
<__main__.Dog object at 0x1004ccc90>
False
```
* We started by defining a new Dog() class, then created two new dogs,each assigned
to different objects.
* So to create an instance of a class, you use the class name,followed by parentheses.
* Then to demonstrate that each instance is actually different, we instantiated two more dogs,
assigning each to a variable, then tested if those variables are equal.
```
class Dog:
    pass
a = Dog()
print(type(a))
```
Output:
```
<class '__main__.Dog'>
```
## Instance Methods
* Instance method are defined inside a class and are used to get the contents of and instance.
* They can also be used to perform operations with the attributes of our objects.
## Encapsulation 
* In an object oriented python program, you can restrict access to methods
and variables.
* This can prevent the data from being modified by accident and is known 
as encapsulation.
Let's start with an example.
### Private methods 
* We create a class Car which has two methods : drive() and updateSoftware().
* When a car object is created, it will call the private methods __updateSoftware().
* This function cannot be called on the object directly, only from within class.
* Encapsulation prevents from accessing accidentally, but not intentionally.
* The private attributes and methods are not really hidden, they're renamed 
adding __Car in the beginning of their name.
* The method can actually be called using redcar.__Car__updateSoftware()

### Private Variables
* Variables can be private which can be useful on many occasions.
* A private variable can only be changed within class method and not outside
of the class.
* Objects can hold crucial data for your application and you do not want that
data to be changeable from anywhere in the code.

### Protected Members
* Protected member is accessible only from within the class and it's subclasses.
* By prefixing the name of your member with a single underscore, you're telling 
others "don't touch this, unless you're a subclass".
 







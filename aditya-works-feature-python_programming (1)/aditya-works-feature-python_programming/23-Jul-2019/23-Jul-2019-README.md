## Characteristics of class and it's types 
### Class Variables
* Class variables are defined within the class construction.
* Because they are owned by the class itself,class variable are shared by all
instances of the class.
* They therefore will generally have the same value for every instances
unless you are using the class variable to initialize a variable.
* Defined outside of all the methods, class variables are, by convention,
typically placed right below the class header and before the constructor method 
and other methods.

A class variable alone looks like this : 
```
class Shark:
    animal_type = "fish"
```
* Hence, the variable animal_type is assigned the value "fish".
* We can create an instance of the shark class and print the variable by using 
dot notation : 
```
class Shark:
    animal_type = "fish"
 new_shark = Shark()
 print(new_shark.animal_type)
```
Output:
```
fish
```
Example
```
class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 5
 new_shark = Shark()
 print(new_shark.animal_type)
 print(new_shark.location)
 print(new_shark.followers)
```
Output:
```
fish
ocean 
5
```
* The instance of new_shark is able to access all the class variables and 
print them out when we run the program.
* Class variables allow us to define variable upon constructing the class.
* These variables and their associated values are then accessible to each 
instance of the class.

### Instance Variables 
* Instance variables are owned by instance of the class.
* This means that for each object or instance of a class, the instance variables are
different.
* Unlike class variables,instances variables are defined within methods.
* In the shark class example below, name and age are instance variables:
```
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
* When we create a Shark object, we will have to define these variables,
which are passed as parameters within the constructor method or another method.
```
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 new_shark = Shark("Sammy", 5)
 print(new_shark.name)
 print(new_shark.age)
```
As with class variables, we can similarly call to print instance variables :
```
Sammy
5
```
The output we receive is made up of the values of the variables that we initialized for the object
instance of new_shark . 
* Let's create another object of the shark class called stevie :
```
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 new_shark = Shark("sammy",5)
 print(new_shark.name)
 print(new_shark.age)
 stevie = Shark("Stevie", 8)
 print(stevie.name)
 print(stevie.age)
```
* The stevie object, like the new_shark object passes the parameters specific
for that instance of the Shark class to assign values to the instance variables.
* Instances variables, owned by objects of the class, allow for each object or instance
to have different values assigned to those variables.
## Behaviour of class and it's type :
### Instance Methods 
* The first method on MyClass,called method,is a regular instance method.
* You can see the method takes one parameter,self, which point to an intances
of MyClass when the method is called.
* Through the self parameter, instance methods can freely access attributes and 
other methods on the same object.
* This gives them a lot of power when it comes to modifying an object's state.
* Not only can they modify object state, instance methods can also access
the class itself through the self.__class__ attribute.
* This means instance methods can also modify class state.
### Class Method
* Let's compare that to the method,MyClass.classmethod.
* I marked this method with a @classmethod decorator to flag it as a class method.
* Instead of accepting a self parameter, class methods take a cls paraneter
that points to the class - and not the object instance - when the method is called.
* Because the class method only has access to this cls argument, it can't modify
object instance state.
* That would require access tp self.
* However,class methods can still modify class state that apploes across all
instances of the class.
### Static Methods
* The third method, Myclass.staticmethod was marked with a @staticmethod
decorator to flag it as a static method.
* This type of method takes neither a self nor a cls parameter 
* Therefore a static method can neither modify object state nor class state.
* Static methods are restricted in what data they can access and they're primarly a 
way to namespace your methods.


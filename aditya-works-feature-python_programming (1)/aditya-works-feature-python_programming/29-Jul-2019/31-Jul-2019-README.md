## PYTHON METHOD OVERLOADING 
* IN PYTHON WE CAN CREATE A METHOD THAT CAN BE CALLED IN 
DIFFERENT WAYS.
* SO, WE CAN HAVE A METHOD THAT HAS ZERO, ONE OR MORE NUMBER 
OF PARAMETERS AND DEPENDING ON THE METHOD DEFINITION WE CAN CALL
IT WITH ZERO,ONE OR MORE ARGUMENTS.
* Using method overloading techniques we will call the 
method by it's parameters.
#### Example of method overloading
* In the following python program we are overloading the area 
method.
* If there is no argument then it returns 0.
* If we have one argument then it returns square of the value and assumes 
you are computing the area of the square. 
* if we have two arguments then it returns the product of the two
values and assumes you are computing the area of a rectangle.

## Special Function in Python
* Class function that begins with double underscore _ are 
called special function in Python.
* This is because, well, they are not ordinary.
* The `__init__()` function we defined is one of them
* Its gets called every time we create a new object of that 
class. There are a ton of special function in python.
```
p1 = Point(2,3)
print(p1)
<__main__.Point object at 0x00000000031F8CC0>
```
That did not print well. But if we define __str__() method in our class,we can control
how it gets printed.So let's add this to our class.
```
class Point:
    def __init__(self, x = 0,y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
p1 = Point(2,3)
print(p1)
```
## Multiprocessing and its uses
* Parallel processing is getting more attention nowadays.
* As Creating parallel code is a great way to improve performance.
* Python introduced multiprocessing module to let us write parallel code.
* There are plenty of classes in python multiprocessing module for building
a parallel program.
## Uses of multiprocessing
1. Using multiprocessing shared resources will efficiently used.
2. Execution time can be reduced using multiprocessing.
3. We can achieved parallel processing using multiprocessing

## Special Variable in Python

* Since there is no main() function in Python, when the command to run a python
program is given to interpreter, the code that is at level 0 indentation
is to be executed.
* However before doing that, it will define a few special variables.
* __name__ is one such special variable.
* if the source file is executed as the main program the interpreter sets the
__name__ variable to have a value "__main__".
* if this file is being imported from another module, __name__ will be 
set to the module's name.
* __name__ is a built-in variable which evaluates to the name of the 
current module.
* Thus it can be used to check whether the current script 
is being run on its own or being imported somewhere else by
combining it with if statement.
 ```
 Attribute                   Meaning 
 __doc__                    The function documentation string
 
 __name__                   The function's name
 
 __qualname__               The function's qualified name
 
 __module__                 The name of the module the function
                            was defined in, or None if unavailable.
                            
 __defaults__               A tuple containing default argument values for
                            those arguments that hae defaults.

 __code__                   The code object representing the compiled function
                            body.

__globals__                A reference to the dictionary that holds the function's
                            global variable

__dict__                   The namespace supporting arbitrary function attributes.

__closure__                None or tuple of cells that contain bindings 
                           for the function's free variables.

__annotations__           A dict containing annotations of parameters.
                           The keys of the dict are the parameter
                           names and 'return' for the return annotation     
                                                                                                     
__kwdefaults__            A dict containing defaults for keyword-only parameters.                           
 ```

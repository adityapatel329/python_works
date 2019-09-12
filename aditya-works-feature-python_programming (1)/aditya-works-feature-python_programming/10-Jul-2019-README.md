## Python Modules
* Modules refer to a file containing Python statements and definitions.
* A file containing Python code, for e,g: example.py is called a module
  and its module name would be example.
* We use modules to break down large programs into small manageable and
  organized files. Furthermore,modules provide reusability of code.
* We can define our most used functions in a module and import
  it,instead of copying their definitions into different programs.

#### Creating a module 
```
#name of the file is addition

def add(a, b):
    result=a+b
    return result
```
Here, we have defined a function add() inside a module named addition.
The function takes in two numbers and returns sum. 

#### Importing a module
* We can import the definitions inside a module to another or the interactive interpreter in python.
* We use the import keyword to do this.
* To import our previously defined module addition we type the following in the Python prompt.
```
>>> import addition
```
* This does not enter the names of the functions defined in addition directly in the current symbol table.if only enters
the module name addition there.

* Using the module names we can access the function using the dot . operator. 
For example:
```
>>> addition.add(4,5.5)
9.5
```
* Standard modules can be imported the same way as we import our user-defined modules.
* There are various ways to import modules.THey are listed as follows.

## Python import statement
* We can import a module using import statement and access the definitions inside it using the dot operator as
described above. Here is an example.
```
# import statement example
# to import standard module math

import math 
print("The value of pi is", math.pi)
```
Output:
```
The value of pi is  3.141592653589793
```
### Import with renaming 
* We can import a module by renaming it as follows.
```
# import module by renaming it

import math as m
print("The value of pi is",m.pi)

```
* We have renamed the math module as m.
* This can save us typing time in some cases.
### Python from ... import statement 
```
# import only pi from math module 

from math import pi
print("The value of pi is",pi)

```
* We imported only the attribute pi from the module.
* In such case we don't use the dot operator.
* We could have imported multiple attributes as follows.
```
>>> from math import pi,e
>>> pi
3.141592653589793
>>> e
2.718281828459045
```
#### Import all names
* We can import all names form a module using the following construct.
```
from math import *
print("This value of pi is",pi)
```
* We imported all the definitions from the math module.
* This makes all names except those beginning with an underscore, visible in our scope.
* Importing everything with asterisk(*) symbol is not good programming practice.
* This can lead to duplicate definitions for an identifier.

### Python Module Search Path
* While importing a module,Python looks at several places.
* Interpreter first look for a built-in module then (if not found)
into a list of directories defined in sys.path. 
* The search is in this order.
* The current directory 
* PYTHONPATH (an environment variable with a list of directory)
* The installation-dependent default directory.
```
>>> import sys
>>> sys.path
['',
'C:\\Python33\\Lib\\idlelib',
'C:\\Windows\\system32\\python33.zip',
'C:\\Python33\\DLLs',
'C:\\Python33\\lib',
'C:\\Python33',
'C:\\Python33\\lib\\site-packages']
```
* We can add modify this list to add our own path.
### Reloading a module
* The python interpreter imports a module only once during a session.
* This makes things more efficient.
* Here is an example to show how this works.
Suppose we have the following code in a module 
```
# This module shows the effect of
# multiple imports amd reload
print("This code get executed")
```
Now wee see the effect of multiple imports.
```
>>> import my_module
This code got executed 
>>> import my_module
>>> import my_module
```
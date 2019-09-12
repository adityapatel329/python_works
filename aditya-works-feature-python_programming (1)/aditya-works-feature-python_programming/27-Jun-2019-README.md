## Python Functions
* A function is a block of code which only runs when it is called.
* You can pass data, known as parameters, into a function.
* A function can return data as a result.

## Creating a Function

_In Python a function is defined using the def keyword:_

### Example
```
def my_function():
  print("Hello from a function") 
```
## Calling a Function
_To call a function, use the function name followed by parenthesis:_
### Example
```
def my_function():
  print("Hello from a function")

my_function()

Output:
Hello from a function
```
## Parameters
* Information can be passed to functions as parameter.
* Parameters are specified after the function name, inside the parentheses.
* You can add as many parameters as you want, just separate them with a comma.
* The following example has a function with one parameter (fname).
* When the function is called, we pass along a first name, which is used inside the function to print the full name: 
### Example
```
def my_function(fname):
  print(fname + " Patel")

my_function("Aditya")
my_function("Shubham")
my_function("Rahul") 

Output:
Aditya Patel
Shubham Patel
Rahul Patel 
```
## Default Parameter Value
* The following example shows how to use a default parameter value.
* If we call the function without parameter, it uses the default value:
### Example
```
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

Output:
I am from Sweden
I am from India
I am from Norway
I am from Brazil 
```
## Passing a List as a Parameter 
You can send any data types of parameter to a function(string,number,list,dictionary etc.),and it will be treated as the same
data types inside the function.\

E.g. if you send a List as a parameter, it will still be a list when it reaches the function:

### Example 
```
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

Output :
apple
banana 
cherry
```
### Return Values
To let a function return a value,use the return statement:

### Example
```
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
 
Output:
15
25
45
```
## Procedural Programming Approach in Python 

How python perform procedural programming approach 
* Tasks are treated as step-by-step iterations where common tasks are placed in functions that are called as needed.
* This coding style favors iteration, sequencing, selection, and modularization.
* Python excels in implementing this particular paradigm.

## Using the procedural coding style 
* The procedural style relies on procedure calls to create modularized code.
* This approach simplifies your application code by breaking it into small pieces that a developer can view easily.
* Even though procedural coding is an older form of application development, it’s still a viable approach for tasks that lend themselves to step-by-step execution.
* Here’s an example of the procedural coding style using my_list:
```
any_list=[1,2,3]
def do_add(any_list):
    sum = 0
    for x in any_list:
        sum += x
    return sum
print(do_add(any_list))
```
* The use of a function, do_add(), simplifies the overall code in this case.
* The execution is still systematic, but the code is easier to understand because it’s broken into chunks.

## Module in python
* Consider a module to be the same as a code library.
* A file containing a set of functions you want to include in your application.

## Create a Module
To create a module just save the code you want in a file with the file extension .py:

### Example
```
Save this code in a file named mymodule.py

def greeting(name):
  print("Hello, " + name) 
```
## Use a Module 
Now we can use the module we just created, by using the import statement:

### Example
```
Import the module named mymodule, and call the greeting function:

import mymodule
mymodule.greeting("Aditya")

Output:
Hello, Aditya
```
## Variables in Module
The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
### Example 
```
Save this code in the file mymodule.py

person1 = {
  "name": "Aditya",
  "age": 21,
  "country": "India"
} 
```
Import the module named mymodule, and access the person1 dictionary:
```
import mymodule
a = mymodule.person1["age"]
print(a)

Output:
21
```
## Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.

### Example 
Import and use the platform module:
```
import platform
x = platform.system()
print(x) 

Output:
Windows
```
### Example of Calling Two Module 
module1.py
```
import module2
from module2 import *
def add(number1, number2):
    return (number1+number2)

def sub(number1,number2):
    return (number1-number2)
    

a = add(10, 20)
s = sub(20, 20)
m = module2.mul(a, s)
print("Addition:", a)
print("Subtraction:", s)
print("Multiplication:", m)
```
module2.py
```
def mul(x,y):
    return (x*y)
```



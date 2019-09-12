## Lambda Functions in Python

#### Why are lambda functions ?
* In Python we use the ``lambda`` keyword to declare an anonymous function.
* An anonymous function refers to a function declared with no name.
* The following are the characteristics of Python lambda functions : 
1. A lambda function can take any numbers of arguments, but they contain
only a single expression.
2. Lambda functions can be used to return functions objects.
3. Syntactically, lambda functions are restricted to only a single expression.

#### Creating a Lambda Function
We use the following syntax to declare a lambda function :

``lambda arguments(s): expression``

The lambda operator cannot have any statements and it returns a
function object that we can assign to any variable.

For example:
```
remainder = lambda num: num % 2
print(remainder(5))
```
Output:
```
1
```
* In this code the lambda num: num % 2 is the lambda function
* The num is the arguments while num%2 is the expression that is evaluated
and the result of the expression is returned.
* The expression gets the modulus of the input parameter by 2.
* Providing 5 as the parameter, which is divided by 2, we get a remainder of 1.
* lambda function returns a function object which is assigned to the identifier
remainder.

`` lambda num: num % 2``

Is similar to the following :
```
def remainder(num):
    return num % 2
```

#### Why use lambda Functions?
* Lambda functions are used when you need a function for a short period of time.
* This is commonly used when you want to pass a function as an argument to higher - order
functions,that is, functions that take other functions as their arguments.
* The use of anonymous function inside another function is explained in the following example:
```
def testfunc(num):
    return lambda x : x*num
 result1 = testfunc(10)
 print(result(9))
```
Output:
```
90
```
## The filter() Function
The Python's filter() function takes a lambda function together 
with a list as the arguments

`filter(object, iterable)`

* The `object` here should be a lambda function which returns a boolean value.
* The object will be called for every time in the iterable to do the evaluation.
* The results is either a `True` or a `False` for every time.
* A lambda function, along with list to be evaluated, is passed to the filter()
function.
* The filter() function returns a list of those elements that return `True` when evaluated 
by the lambda function.
Consider the example given below:
```
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

filtered_list = list(filter(lambda num: (num > 7), numbers_list))

print(filtered_list)
```
Output: 
```
[8, 10, 11, 12, 13, 17, 21]
```
* In the above example, we have created a list named number_list with a list of
integer.
* We have created a lambda function to check for the integers that are greater than 7.
* The lambda function has been passed to the filter() function as the argument
and the results from this filtering have been saved into a new list named 
`filtered_list`

## The map() Function
* The map() function is another built0in function that take a function object
and a list.

`map(object, iterable_1,iterable_2, ...)`

* The iterable to the map() function can be a dictionary, a list etc.
* The map() function basically maps every time in the input iterable to
the corresponding item in the output iterable, according to the logic defined
by the lambda function.
```
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

mapped_list = list(map(lambda num: num % 2, numbers_list))

print(mapped_list)
```
Output:
```
[0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1]
```
* In the above example ,we have a list number_list, which consists of random number.
* When then call the map() function and pass it a lambda function as the arguments.
* The lambda function calculates the remainder after dividing each number by 2.
* The result of the mapping is stored in a list named mapped_list 
## The reduce() Function
* The reduce() function in Python takes in a function and a arguments.
* The function is called with a lambda function and a list and a new
reduced result is returned.
* This perform a repetitive operation over the paris of the list.
```
from functools import reduce
li= [5, 8, 10, 20, 50, 100]
sum =reduce((lambda x,y : x + y), li)
print(sum)
```
Output:
```
193
```
* Here the result of previous two elements are added to the next element
and this goes on till the end of the list like 
(((((5+8)+10)+20)+50)+100).

## Python Exceptions : 
* A python program terminates as soon as it encounters an error.
* In Python, an error can be a syntax or an exception.

#### Exception versus Syntax Errors
* Syntax errors occur when the parser detects an incorrect statement.
```
print( 0 / 0))
             ^
SyntaxError : invalid syntax
```  
* The arrow indicates where the parser ran into the syntax error.
* In this example there was one bracket too many.
Remove it and run your code again:
```
>>>print( 0 / 0)
ZeroDivisionError: integer division or modulo by zero
```
* This time, you ran into an exception error.
* This type of error occurs whenever syntactically correct 
Python code result in an error.
* The last line of the message indicated what type of exception error you 
ran into.

## Raising an Exception
* We can use raise to throw an exception if a condition occurs.
* The statement can be complemented with a custom exception.
* if you want to throw an error when a certain condition occurs using raise,
you could go about it like this:
```
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
```
Output:
```
Traceback (most recent call last):
    File "<input>", line 4, in <module>
Exception: x should not exceed 5. The value of x was: 10
```
## The AssertionError Exception
* Instead of waiting for a program to crash midway, you can also start by making an assertion in Python.
* We assert that a certain condition is met. If this condition turns out to be True, then that is excellent! The program can continue.
* If the condition turns out to be False, you can have the program throw an AssertionError exception.
Example:
```
import sys
assert ('linux' in sys.platform), "This code runs on Linux only.
```
Output:
```
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError: This code runs on Linux onl
```

## The try and except Block: Handling Exceptions
* The try and except block in Python is used to catch and handle exceptions. 
* Python executes code following the try statement as a “normal” part of the program.
* The code that follows the except statement is the program’s response to any exceptions in the preceding try clause.
* As you saw earlier, when syntactically correct code runs into an error, Python will throw an exception error.
Example :
```
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')
try:
    linux_interaction()
except:
    print('linux function was not executed')
```
Output:
```
Linux function was not executed
```
## The else Clause
* In Python, using the else statement, you can instruct a program to execute a certain block of code only in the absence of exceptions.
Example :
```
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause.')
```
Output:
```
Executing the else clause.
```
## Finally Block
* Imagine that you always had to implement some sort of action to clean up after executing your code.
* Python enables you to do so using the finally clause.

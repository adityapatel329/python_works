## Python Nested Functions
* Functions are one of the "first-classes citizen" of Python, which means that functions are at the same level as other Python objects like
integer,strings,modules,etc.
* They can be created and destroyed dynamically,passed other functions,
returned as values,etc.

* Python supports the concept of a "nested function" or "inner function", which is simply a function defined inside another function
* There are various reasons as to why one would like to create a function inside another function
* The inner function is able to access the variables within the enclosing scope. 

## Defining an Inner Function
To define an inner function in Python,we simply create a function inside another 
function using the Python's "def" keyword.

### Example
```
def function1():
    print("Hello from outer function")
    def function2():
        print("Hello from inner function")
     function2()
  
function1()

Output:
Hello from outer function
Hello from inner function
```
* In the above example, function2() has been defined inside function1(),making it an
inner function.To call function2(),we must first call function1(). THe function1()
will then go ahead and call function2() as it has been defined inside it.

* It is important to mention that the outer function has to be called in order for the inner function to execute.
* If the outer function is not called, the inner function will never execute.
* To demonstrate this,we will modify the above code to the following and run it:
```
def function1():
    print("Hello from outer function")
    def function2():
        print("Hello from inner function")
    function2()

Output:
The code will return nothing when executed!
```
Here is another example:
```
def mul(x):
    def num2(y):
        return x * y
     return num2
res=mul(10)

print(res(5))

Output:
50
```
* The code returns the multiplication of the two numbers,that is 10 ans 5.
* The example shows that an inner function is able to access variable accessible in the outer function.

##### _What if we attempt to change the variables of the outer function from inside the inner function? Let us see what happens:_

```
def function1():
    x=2
    def function2(a):
        x=6
        print(a+x)
     print(x)
     function2(3)
function1()

Output:
2
9
```
* The output shows that it is possible for us to display the value of a variable defined 
within the outer function from the inner function, but not change it.
* The statement x=6 helped us create a new variable x inside function function2() rather than changing
the value of variable x defined in the outer function1().

## Returning Multiple Values in Python

In Python, we can return multiple values from a function. Following are different ways

#### _Using Object:_
This is similar to C/C++ and Java, we can create a class (in C, struct) to hold multiple values and return an object of the class.

### Example
```
class Test: 
    def __init__(self): 
        self.str = "aditya"
        self.x = 20   
  

def fun(): 
    return Test() 
      
t = fun()  
print(t.str) 
print(t.x)

Output:
aditya
20 
```
#### _Using Tuple:_
A Tuple is a comma separated sequence of items. It is created with or without (). Tuples are immutable. See this for details of tuple and list.

### Example
``` 
def fun(): 
    str = "aditya"
    x   = 20
    return str, x;    
  
str, x = fun()  
print(str) 
print(x)

Output:
aditya
20
```
#### _Using a List:_
 A list is like an array of items created using square brackets. They are different from arrays as they can contain items of different types. Lists are different from tuples as they mutable.
 ```
 def fun(): 
    str = "aditya"
    x = 20   
    return [str, x]
     
list = fun()  
print(list) 

Output:
['aditya','20']
 ```
 #### _Using a Dictionary_
 A Dictionary is similar to hash or map in other languages. See this for details of dictionary.
```
def fun(): 
    d = dict();  
    d['str'] = "adiya"
    d['x']   = 20
    return d 
     
d = fun()  
print(d)

Output:
 {'x': 20, 'str': 'aditya'}
``` 
## Python Lambda
* A lambda function is a small anonymous function.
* A lambda function can take any number of arguments, but can only have one expression.

#### _Syntax_
```
lambda arguments : expression
```
The expression is executed and the result is returned :

### Example 
```
x= lambda a:a+10
print(x(5))

Output:
15
```
Lambda function can take any number of arguments:
### Example
```
x=lambda a,b :a * b
print(x(5,6))

Output:
30
```
## The Break Statement :
* The break statement terminates the loop containing it.
* Control of the program flows to the statement immediately after the body of the loop.
* If break statement is inside a nested loop (loop inside another loop), break will terminate the innermost loop.

#### _Syntax_
```
    break
```
### Example 
```
for val in "string":
    if val == "i":
        break
    print(val)
    
print("The end")

Output:
s
t
r
The end
```
* In this program, we iterate through the "string" sequence.
* We check if the letter is "i", upon which we break from the loop.
* Hence, we see in our output that all the letters up till "i" gets printed.
* After that, the loop terminates.

## Python continue statement 
* The continue statement is used to skip the rest of the code inside a loop for the current iteration only.
* Loop does not terminate but continues on with the next iteration.
#### _Syntax_
```
  oontinue 
```
### Example
```
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")

Output:
s
t
r
n
g
The end
```
* This program is same as the above example except the break statement has been replaced with continue.
* We continue with the loop, if the string is "i", not executing the rest of the block.
* Hence, we see in our output that all the letters except "i" gets printed.

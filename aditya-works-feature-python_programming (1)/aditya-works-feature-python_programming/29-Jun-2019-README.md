## Python function arguments:
* The first thing a programmer must be aware of is that parameters and arguments are clearly two different things although
  people use them synonymously.
* Parameters are the variables that are defined or used inside parentheses while defining a function, whereas arguments 
  are the value passed for these parameters while calling a function.
* Arguments are the values that are passed to the function at run-time so that the function can do the designated task  
  using these values.

### Example
```
def function_name(arg_1,arg_2):{Function parameters}
  ....
  ....
  ....
  return[expession]
  
function_name(arg_1,arg_2)}function call ,{Function arguments}
```
Now that you know about Python function arguments and parameters, let’s have a look at a simple program to highlight more 
before discussing the types of arguments that can be passed to a function.
```
#Defining a function first to return the value of parameter
def display(x):  #x is the parameter
  return x

#Calling the function and supplying arguments
print ("Hello " + display('Aditya'))  #'Aditya' is the argument
Output:
Hello Aditya
```
In this example, we have defined a function with parameter ‘x’. Basically, this function will return whatever the value
 is passed as an argument while calling.

## Types of function arguments in Python
There are three types of function arguments which we can call a function.
1. Default Arguments
2. Requires Arguments 
2. Keyword Arguments 
3. Variable-length Arguments 

## Python Default Arguments 
* Sometimes we may want to use parameters in a function that takes default values in case the user doesn’t want to provide 
   a value for them.
* For this we can use default arguments which assume a default 
  value if a value is not supplied as an argument while calling 
  the function.
* An assignment operator ‘=’ is used to give a default value to an argument. 
  Here is an example.  
### Example
```
def sum(a=4, b=2): #2 is supplied as default argument
  """ This function will print sum of two numbers
      if the arguments are not supplied
      it will add the default value """
  print (a+b)

sum(1,2)  #calling with arguments
sum( )    #calling without arguments

Output 
3
6
```
* In the program above, default arguments 2 and 4 are supplied to the function.
* First, the user has provided the arguments 1 and 2, hence the function prints their sum which is 3.
* In the second call, the user has not provided the arguments. Thus the function takes the default arguments and prints their sum.

## Required Arguments 
* Required arguments are the arguments passed to a function in correct positional order.
*  Here, the number of arguments in the function call should match exactly with the function definition.

_To call the function printme(), you definitely need to pass one argument, otherwise it gives a syntax error as follows −_
### Example 
```
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme()

Output:
TypeError: printme() takes exactly 1 argument (0 given)
```
## Keyword arguments
* Keyword arguments are related to the function calls. 
* When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name.
* This allows you to skip arguments or place them out of order 
  coz the Python interpreter is able to use the keywords provided to match the values with parameters.
* You can also make keywords calls to the printime() function in the following ways -
```
def print_name(name1, name2):
  """ This function prints the name """
  print (name1 + " and " + name2 + " are friends")

#calling the function
print_name(name2 = 'Aditya',name1 = 'Shubam')

Output:
Shubam and Aditya are friends
``` 
* Notice in above example, if we had supplied arguments as print_name('Aditya','Shubam')
and the output would have been Aditya and Shubam are friends as the values would have been assigned by arguments position.

* But using keyword arguments by specifying the name of the argument itself, we don’t have to worry about their position.
* This makes using function easier as we don’t need to worry about the order of arguments.

## Variable-length Arguments
* You may need to process a function for more arguments than you specified while defining the function.

* These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.

Syntax for a function with non-keyword variable arguments is this −
```
def functionname([formal_args,] *var_args_tuple ):
   "function_docstring"
   function_suite
   return [expression]
```
* An asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable arguments.

* This tuple remains empty if no additional arguments are specified during the function call. Following is a simple example −
```
# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

Output:
Output is:
10
Output is:
70
60
50
```
## Keyword Variable number of arguments of function
* The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. 
* It is used to pass a non-keyworded, variable-length argument list.
* The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
* What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined.
* With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
* For example : we want to make a multiply function that takes any number of arguments and able to multiply them all together. It can be done using *args.
* Using the *, the variable that we associate with the * becomes an iterable meaning you can do things like iterate over it, run some higher order functions such as map and filter, etc.

### Example for usage of *arg
```

# Python program to illustrate   
# *args for variable number of arguments 
def myFun(*argv):  
    for arg in argv:  
        print (arg) 
    
myFun('Hello', 'Welcome', 'to', 'AKST')
  
Output:
Hello 
Welcome 
to
AKST
``` 
### **kwargs
* The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list
* The reason is because the double star allows us to pass through keyword arguments (and any number of them).
* A keyword argument is where you provide a name to the variable as you pass it into te function.

### Example for usage of **kwargs
```
def mul(**z):
    value=1
    for key,v in z.items():
        value*=v
    return value
print(mul(num_one=10,num_two=2,num_three=4))
 
Output:
80
```





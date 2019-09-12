### Python Input and Output 
In python,we have the following two functions to handle input from a user and system.
1. input(prompt) to accept input from a user.
2. print() to display output on a console.

**The input is nothing but some value from a system user.** For example
,if you want to perform an addition of two numbers on the calculator you need to provide two number to the calculator, 
 those two number is nothing but an input provided by the user to a calculator program.
 
 **The input() function reads a line entered on a console by an input device such as a keyborad and convert it into a string** and 
 returns it.You can use this input string in your python code.
 
 There are different types of Input, and that comes in various ways. For example:-
 * Input stems from the keyboard :- the user entered some value using a keyboard.
 * Input using mouse click or movement :- you clicked on the radio button or some drop-down list
 and chosen an option from it.
 
##### _There are two ways to reading inputs._
1. User Interface
2. Command line environment

### Input Using User Interface 
Let see how to accept employee data from the user using the input function and displaying it using the print function.

Example:
```
    name    = input("Enter Employee Name")
    salary  = input("Enter salary")
    company = input ("Enter Company name")
    print("Printing Employee Details")
    print ("Name", "Salary", "Company")
    print (name, salary, company)
```
Output:
```
    Enter Employee Name Aditya
    Enter your salary 8000
    Enter Company name 1rivet
    Printing Employee Details
    Name Salary Company
     Aditya  8000  1rivet
```
### Input Using Command Line Interface 
* User enters the values in the Console and that value is then used in the program as it was required.
* To Take input in command line there are one module named Sys
* Sys module contain a variable called argv
* Argv is a list type to prove the argv list type above example can be used
```
from sys import argv      Output:
print(type(argv))        <class 'list'>        
```
Program to print command line information
```
from sys import argv
print("The number of command line arguments",len(argv))
print("The lsit of command line arguments:",argv)
print("The command line arguments one by one:")
for x in argv:
    print(x)
```
Output:
```
Python37-32>python arg.py 10 20 30 40
The number of command line arguments 5
The lsit of command line arguments: ['arg.py', '10', '20', '30', '40']
The command line arguments one by one:
<class 'list'>
arg.py
10
20
30
40
```
### Argparse Library
* Argparse is a module thats allows for neat and familiar option and argument parsing for our python programs
* Automatically generates the usage.
* Has inbuilt help functions
* Auto formats the output for the console.
### Positional Arguments
* Positional arguments are required arguments that we need for our program to complete.
* Positional arguments do not require the dash(-) because it is not an option.
### Optional Arguments
* As their title indicates, the optional arguments are optional .
* The -h option is already inbuilt by default 
* We can create as many as we like and argparse will handle it .
* parser.add_arguments("--quiet",help="help text",action="sore_true")

##S teps To Run The Code 
1. Run main.py file
2. Than type this following command  
 python main.py -n1 10 -n2 20 -o add 
 it will add two number 
3. if you want help than type following
command \
python main.py -h 
   



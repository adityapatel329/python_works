## Iterative Approach Using Loops 
* There are two common qualifiers used for logical conditions.
* These are sometimes called the universal and existential qualifiers.
* We can call the “for all” and “there exists”.
* We can also call them the “all” and “any” qualifiers.
* A program may involve a state that is best described as a “for all” state, where a number of repetitions of some task are required.
* For example, if we were to write a program to simulate 100 rolls of two dice, the terminating condition for our program would be that we had done the simulation for all 100 rolls.
* We have a choice of two Python statements for expressing this iteration.
* One is the for statement and the other is the while statement.

## Iterative Processing: The for Statement
The simplest for statement looks like this:
```
for variable in iterable :
    suite
```
* The suite is an indented block of statements. Any statement is allowed in the block, including indented for statements
* The variable is a variable name.
* The suite will be executed iteratively with the variable set to each of the values in the given iterable. 
* There are a number of ways of creating the necessary iterable collection of values. 
* The most common is to use the range()

### Example
```
for i in range(6):
    print i+1

Output:
1
2
3
4
5
6
```
* This first example uses range() to create a sequence of 6 values from 0 to just before 6.
* The for statement iterates through the sequence, assigning each value to the local variable i
* The print statement has an expression that adds one to i and prints the resulting value.
## Iterative Processing: The while Statement
The while statement looks like this:
```
while expression :
    suite
```
* The suite is an indented block of statements. Any statement is allowed in the block, including indented while statements.
* As long as the expression is true, the suite is executed.
* This allows us to construct a suite that steps through all of the necessary tasks to reach a terminating condition.
* It is important to note that the suite of statements must include a change to at least one of the variables in the while expression.
### Example 
```
a=1
while a<=10:
    print(a)
    a+=a

Output:
1
2
4
8
```
## Python If ... Else 
##### _Python Conditions and if statements:_ 

Python supports the usual logical conditions from mathematics:
* Equals: a == b
* Not Equals: a != b
* Less than: a < b
* Less than or equal to: a <= b
* Greater than: a > b
* Greater than or equal to: a >= b

_These conditions can be used in several ways, most commonly in "if statements" and loops._

An "if statement" is written by using the if keyword.

### Example 
```
a = 33
b = 200
if b > a:
  print("b is greater than a")
  
Output:
b is greater than a
```
* In this example we use two variables, a and b
* which are used as part of the if statement to test whether b is greater than a.
* As a is 33, and b is 200
* we know that 200 is greater than 33, and so we print to screen that "b is greater than a".
## Elif

The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

### Example 
```
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
Output:
a and b are equal
```
* In this example a is equal to b
* so the first condition is not true, but the elif condition is true,
* so we print to screen that "a and b are equal".
## Else 
The else keyword catches anything which isn't caught by the preceding conditions.
```
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
Output:
a is greater than b 
```
* In this example a is greater than b, so the first condition is not true,
* also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".

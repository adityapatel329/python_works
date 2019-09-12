### Data Types in python
Following data types are supported in python
1. None
2. Numeric
3. List
4. Tuple
5. Set
6. String
7. Range
8. Dictionary
#### None:-
_The None keyword is used to define a null value, or no value at all._

 Example:-\
 Assign the value None to a variable:
```
x = None       Output:- None
print(x)
```
#### Numeric:-
_Numeric can be integers, decimal,complex numbers etc._

```
-Integer
          ex: a=10
-Decimal
          ex: a=10.1
-ComplexNumber
          ex: a=6+5j
-Bool
          ex :a=True
```
#### List:-
_List are ordered sequence that can hold a variety of object types._
_They use [] brackets and commands to separate objects in the list._

Example:-
```
list=[1,2,3,4]     Output:-[1,2,3,4]
print(list)
```
List Methods:-\
_Python has a set of built-in methods that you can use on lists._
* We Can Find Length using len( ) Function.
* We can Append new element using append( ) Function.
* We can Insert new element using insert( )Function.
* We cn Sort the elements using sort( ) Function.
* We can Reverse the elements using reverse( ) Function.\
##### _List Features_
1. Mutable
2. Can have Duplicate values
3. We can perform data manipulation

#### Tuple:-
A tuple is a sequence of immutable Python objects.\
Tuples are sequences, just like lists.

Example:
```
tuple=(1,1,2,3)   Output:- (1,1,2,3)
print(tuple)
```
Tuple Methods:-\
_Python has a set of built-in methods that you can use on Tuple._
* We can Find Length using len( ) Function.
* We can perform Concatenation to tuple using "+" Symbol.
* We can make repetition operation using "*" Symbol.
##### _Tuple Features_
1. Immutable
2. Can have Duplicate values

#### Set:-
Sets are unordered collection of unique elements.\
Meaning there can only be one representative of the same object.
Example:
```
set={1,2,3}   Output:- {1,2,3}
print(set)
```
Set Methods:-\
_Python has a set of built-in methods that you can use on Set._
* add( )  Adds an elements to the set.
* clear( ) Removes all the elements from the set.
* copy( ) Returns a copy of the set.
* pop( ) Removes an elements from the set.
* remove( ) Removes the specified element.
#### _Set Features_
1. Mutable
2. Unordered
#### String:-\
A string in Python is a sequence of characters. \
It is a derived data type.

Example:
```
string="Aditya"   Output:- "Aditya"
print(string)
```
#### Range:-
The range() function is used to generate a sequence of numbers over time. \
At its simplest, it accepts an integer and returns a range object (a type of iterable).

Example:
```
range(5)
range(0, 5)
list(range(5)) #list() call is not required in Python 2
[0, 1, 2, 3, 4]
```
#### Dictionary:-
Dictionaries are unordered mapping for storing objects,dictionaries use a key-value pairing instead.\
This key-value pair allows user to quickly grab objects without needing to know an index location.
Example: 
```
my_dict = {'name':'Jack', 'age': 26}    Output:- Jack                                                   26
print(my_dict['name'])                            26
print(my_dict.get('age'))  
```
Dictionary Methods:-\
_Python has a set of built-in methods that you can use on Dictionary._
* clear( ) Remove all items from the dictionary.
* copy( )  Return a shallow copy of the dictionary.
* items( ) Return t new view of the dictionary's items.
* keys( )  Return a new view of the dictionary's keys.
* popitem() Remove and return an arbitary item(key,value).
#### _Dictionary Feature_
1. Mutable
2. Unordered 
### Python Operators
Operators are used to perform operations on variables and values.\
Python divides the operators in the following groups:
1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators 
5. Identity operators
6. Membership operators
7. Bitwise operators
#### Python Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:
```
Operator   Name            Example
  +        Addition          x+y
  -        Subtraction       x-y
  * 	   Multiplication    x*y
  /        Division          x/y
  %        Modulus           x%y
  **       Exponentiation    x**y
  //       Floor division    x//y
```
#### Python Assignment Operators
Assignment operators are used to assign values to variables:
```
Operator        Example
   =              x=5
   +=             x+=3
   -=             x-=3
   *=             x*=3
   /=             x/=3
   %=             x%=3
   //=            x//=3
   **=            x**=3 
```
#### Python Comparison Operators
Comparison operators are used to compare two values:
```
Operator       Name               Example
  ==           Equal               x==y
  !=           Not equal           x!=y
  >            Greater than        x>y
  <            Less than           x<y
  >=           Greater than or     x>=y
               equal to       
  <=           Less than or        x<=y
               equal to     
```
#### _Python Logical Operators_
Logical operators are used to combine conditional statements:
```
Operator     Description                    Example
  and        Returns True if                x<5 and x<10
             both statements are true
  or         Returns True if one            x<5 or x<4
             of the statements is true     
  not        Reverse the result,returns     not(x<5 and x<10)
             False if the result is true   
```
#### _Python Identity Operators_
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
```
Operator         Description                  Example
   is            Returns true if both          x is y
                 variables are the same
                 objectaqw340
   is not        Returns true if both          x is not y 
                 variable are not the 
                 same oobject 
```
#### _Python Membership Operators_
Membership operators are used to test if a sequence is presented in an object:
```
Operator           Description                        Example
   in              Reuturns True if a sequence        x in y
                   with the specified value is 
                   present in the object
   not in          Returns True if a sequence with the  x not in y  
                   specified values is not present in
                   the object
```
#### _Python Bitwise Operators_
Bitwise operators are used to compare binary numbers:
```
Operator      Name       Description
  &           AND        Sets each bit to 1 if both bits are 1
  |           OR         Sets each bit to 1 if one of two bits are 1
  ^           XOR        Sets each bit to 1 if only one of two bits is 1
  ~           NOT        Inverts all the bits 
  <<          Left       Shift left by pusing zeros in from the right and let   
              Shift      the leftmost bits fall off 
  >>          Right      Shift right by pusing copies of the leftmost bit in
              Shift      form the left, and let the rightmost bits fall off
```

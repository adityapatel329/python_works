## Tuple:-
A tuple is a sequence of immutable Python objects.\
Tuples are sequences, just like lists.
### _Tuple Methods:-_
_Python has a set of built-in methods that you can use on Tuple._
* We can Find Length using len( ) Function.
* We can perform Concatenation to tuple using "+" Symbol.
* We can make repetition operation using "*" Symbol.
### _Tuple Features_
1. Immutable
2. Can have Duplicate values

### Creating a Tuple
Syntax:
```
variable_name = (elements..)

ex: 
a=(1,2,3,4,5)
print(a)

Output:
(1,2,3,4,5)
```
A tuple can also be created without using parentheses. This is known as tuple packing
```
my_tup=1,2,3,"adi"
print(my_tup)

Output:
(1,2,3,"adi")

#tuple unpacking is also possible
a,b,c=my_tup
print(a)
```
```
my_tuple = ("hello")
print(type(my_tuple))  # <class 'str'>

# Creating a tuple having one element
my_tuple = ("hello",)  
print(type(my_tuple))  # <class 'tuple'> 

# Parentheses is optional
my_tuple = "hello",
print(type(my_tuple))  # <class 'tuple'> 
```
### Accessing/Removing Elements from Tuple
There are various ways in which we can access the elements of a tuple.
#### Indexing

* We can use the index operator [] to access an item in a tuple where the index starts from 0.
* So, a tuple having 6 elements will have indices from 0 to 5.
* Trying to access an element outside of tuple (for example, 6, 7,...) will raise an IndexError.
* The index must be an integer;so we cannot use float or other types. This will result in TypeError.
* Likewise, nested tuples are accessed using nested indexing, as shown in the example below.

### Example
```
my_tuple=('a','d','i','t','y','a')
print(my_tuple[0]) # 'a'
print(my_tuple[5]) # 'a'

# IndexError : list index out of range
#print(my_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple

#nested tuple
n_tuple=("mouse",[8,4,6],(1,2,3))

#nested index
print(n_tuple[0][3]) # 's'
print(n_tuple[1][1]) # 4
```
#### Negative Indexing
* Python allows negative indexing for its sequences.
* The index of -1 refers to the last item, -2 to the second last item and so on.
```
my_tuple=('a','d','i','t','y','a')
print(my_tuple[-1])
print(my_tuple[-6])

Output:
'a'
'a'
```
#### Slicing 
We can access a range of items in a tuple by using the slicing operator - colon ":".
```
my_tuple=('p','r','o','g','r','a','m','i','z')

#element 2nd to 4th
print(my_tuple[1:4])
print(my_tuple[:-7])
print(my_tuple[7:])
print(my_tuple[:])
Output:
('r','o','g')
('p','r')
('i','z')
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
```
* Slicing can be best visualized by considering the index to be between the elements as shown below.
* So if we want to access a range, we need the index that will slice the portion from the tuple.

[Imgur](https://i.imgur.com/WgYcoB1.jpg)

#### Changing a Tuple
* Unlike lists, tuples are immutable.
* This means that elements of a tuple cannot be changed once it has been assigned.
* But, if the element is itself a mutable data type like list,its nested items can be changed.

We can also assign a tuple to different values(reassignment).
```
my_tuple=(4,2,3,[6,5])

#TypeError: 'tuple' object does not support item assignment 
#my_tuple[1]=9

# However ,item of mutable element can be changed
my_tuple[3][0]=9
print(my_tuple)

Output:
(4,2,3,[9,5])
```
* We can use + operator to combine two tuples. This is also called concatenation.
* We can also repeat the elements in a tuple for a given number of times using the * operator.
* Both + and * operations result in a new tuple.
```
print((1, 2, 3) + (4, 5, 6))

Output:
(1, 2, 3, 4, 5, 6)
```
```
print(("Repeat",) * 3)

Output:
('Repeat', 'Repeat', 'Repeat')
```
#### Deleting a Tuple
* As discussed above, we cannot change the elements in a tuple.
* That also means we cannot delete or remove items from tuple.

But deleting a tuple entirely is possible using the keyword del.

```
my_tuple = ('p','r','o','g','r','a','m','i','z')

# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del my_tuple[3]

# Can delete an entire tuple
del my_tuple

# NameError: name 'my_tuple' is not defined
print(my_tuple)
```
## Python String 
* A string is a sequence of characters.
* A character is simply a symbol.For example, the English language has 26 characters.
* Computer do not deal with characters, they deal with numbers (binary).
* Even though you may see characters on your screen, internally it is stored and manipulated as a combination of 0's and 1's.

#### How to create a string in Python ?
Strings can be created by enclosing characters inside a single quote or double quotes
```
my_string ='Hello'
print(my_string)

my_string="Hello"
print(my_string)

my_string ='''Hello'''
print(my_string)

my_string = """Hello, welcome to 
               the world of Python"""
print(my_string)
```
Output:
```
Hello
Hello 
Hello
Hello, welcome to 
               the world of Python
```
#### How to access characters in a string ?
* We can access individual character using indexing and a range of character using slicing.
* Index Starts from 0. Trying to access a character out of index range will rise an IndexError.
* The index must be an integer. We can't use float or other types, this will result into TypeError.
```
str="aditya"
print(str)
print(str[0])
print(str[-1])
print(str[1:5])
```
Output:
```
'aditya'
'a'
'a'
'dity'
```
#### How to change or delete a string ?
* String are immutable.
* This means that elements of a string cannot be changed once it has been assigned.
```
my_string="aditya"
my_string[4]='g'

TypeError : 'str' object does not support item assigment 
```
We cannot delete or remove characters from a string.But deleting the string entirely is possible using the keyword del.
```
del my_string[1]

TypeError : 'str' object doesn't support item deletion
```
#### Python String Operations
* There are many operations that can be performed with string which makes it one of the most used data types in Python.

##### Concatenation of Two or more String
* Joining of two or more string into a single one is called concatenation.
* The + operator does this in Python. Simply writing two strings literals together also concatenates them.
* The * Operator can be used to repeat string for a given number of times.
```
str1="Hello"
str2="World!"

print('str1 + str2 = ',str1 + str2)

print('str1 * 3 =',str1 * 3)
```
Output:
```
'HelloWorld!'
'HelloHelloHello' 
```
#### Iterating Through String
Using for loop we can iterate through a string. 
```
count=0
for letter in 'Hello World':
    if(letter == 'o'):
        count+=1
print(count,"Letters found")

```
Output:
```
2 Letters found
```
#### String Membership Test
We can test if a sub string exists within a string or not , using the keyword in .
```
'a' in 'program'
True
'at' in 'program'
False
```
#### Built-in functions to Work with Python
* Various built-in function that work with sequence, works with string as well.
* Some of the commonly used ones are enumerate() and len().
```
str = 'cold'
lis = list(enumerate(str))
print('list_enum = ',lis)
print('Length of string = ',len(str))
```
Output
```
list_enum =  [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]
Length of string = 4
```
## Dictionary 
* Python dictionary is an unordered collection of items.
* While other compound data types have only value as an element, a dictionary has a key: value pair.
* Dictionaries are optimized to retrieve values when the key is known.
#### Creating a Dictionary 
* Creating a dictionary is as simple as placing items inside curly braces {} separated by comma.
* An item has a key and the corresponding value expressed as a pair, key: value.
```
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])

```
As you can see above, we can also create a dictionary using the built-in function dict().

#### Accessing the elements from a dictionary
* While indexing is used with other container types to access values, dictionary uses keys. 
* Key can be used either inside square brackets or with the get() method.

The difference while using get() is that it returns None instead of KetError ,if the key is not found.
```
my_dict = {'name':'Aditya','age':19}
print(my_dict.get('name'))
print(my_dict.get('age'))
```
Output:
```
Aditya
19
```
#### Changing or Adding Elements in a Dictionary
* Dictionary are mutable.
* We can add new items or change the value of existing items using assignment operator.
* If the key is already present, values gets updated,else a new key: value pair is added to the dictionary.
```
my_dict={'name':'Aditya','age':20}

my_dict['age']=22
print(my_dict)

my_dict['address'] = 'valsad'
print(my_dict)
```
Output :
```
{'name': 'Aditya', 'age': 22}
{'name': 'Aditya', 'age': 22, 'address': 'valsad'}
```
#### Deleting or Removing Elements from a Dictionary 
* We can remove a particular item in a dictionary by using method pop().
* This method removes as item with the provided key and returns the value.
* This method , popitem() can be used to remove and return arbitrary item(key,value) from the dictionary.
*  All the items can be removed at once using the clear() method.
* We can also use the del keyword to remove individual items or the entire dictionary itself.
```
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares.pop(4))
print(squares)
print(squares.popitem())
print(squares)
del squares[5]  
print(squares)
squares.clear()
print(squares)
del squares
```
Output:
```
16
{1: 1, 2: 4, 3: 9, 5: 25}
(1, 1)
{2: 4, 3: 9, 5: 25}
{2: 4, 3: 9}
{}
```
#### When to use Dictionary 
* Do you need to associate values with keys, so you can look them up efficiently (by key) later on? Use a dictionary.
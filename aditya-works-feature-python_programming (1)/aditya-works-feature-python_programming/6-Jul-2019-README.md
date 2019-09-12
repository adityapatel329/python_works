## List in Python
_List are ordered sequence that can hold a variety of object types._\
_They use [] brackets and commands to separate objects in the list._

### Example:-
```
list=[1,2,3]     Output:-[1,2,3]
print(list)
```
#### List Methods
_Python has a set of built-in methods that you can use on lists._
* We Can Find Length using len( ) Function.
* We can Append new element using append( ) Function.
* We can Insert new element using insert( )Function.
* We cn Sort the elements using sort( ) Function.
* We can Reverse the elements using reverse( ) Function.\
#### List Features
1. Mutable
2. Can have Duplicate values
3. We can perform data manipulation

## Dynamic Input in a list
* We often encounter a situation when we need to take number/string as input from user.

### Example:-
```
lst=[]

n=int(input("Enter your limit : "))

for i in range(n):
    ins=int(input())
    lst.append(ins)

print(lst)
```
Output
```
Enter your limit : 5
0
1
2
3
4
[0, 1, 2, 3, 4]
```
### Example 2:-
```
try: 
    my_list = [] 
    print("Enter elements : ")
    while True: 
        my_list.append(int(input())) 
          
# if input is not-integer, just print the list 
except: 
    print(my_list) 
```
Output
```
5
4
5
4
adi
[5,4,5,4]
```

## Python range() Function
* The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

#### Syntax
```
range(start, stop, step)
```
#### Parameter Values
```

Parameter	     Description
start	Optional. An integer number specifying at which position to start. Default is 0
stop	Optional. An integer number specifying at which position to end.
step	Optional. An integer number specifying the incrementation. Default is 1
```

## Example 
* Create a sequence of numbers from 3 to 5, and print each item in the sequence:
```
x = range(3, 6)
for n in x:
  print(n)
```
Output
```
3
4
5
```
## Example 2
* Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:
```
x = range(3, 20, 2)
for n in x:
  print(n)
```
Output
```
3
5
7
9
11
13
15
17
19
```

## Recursive Functions
* Recursion is a way of programming or coding a problem, in which a function calls itself one or more times in its body.
* Usually, it is returning the return value of this function call. 
*  If a function definition fulfils the condition of recursion, we call this function a recursive function. 
### Termination condition:
* A recursive function has to terminate to be used in a program.
* A recursive function terminates, if with every recursive call the solution of the problem is downsized and moves towards a base case.
* A base case is a case, where the problem can be solved without further recursion.
* A recursion can lead to an infinite loop, if the base case is not met in the calls.
### Example
```
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1

Replacing the calculated values gives us the following expression
4! = 4 * 3 * 2 * 1
```
Now we come to implement the factorial in Python. It's as easy and elegant as the mathematical definition. 
### Example
```
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
fact=factorial(6)
print("Factorial : ",fact)
```
This python scripts output the following results:
```
factorial has been called with n = 5
factorial has been called with n = 4
factorial has been called with n = 3
factorial has been called with n = 2
factorial has been called with n = 1
intermediate result for  2  * factorial( 1 ):  2
intermediate result for  3  * factorial( 2 ):  6
intermediate result for  4  * factorial( 3 ):  24
intermediate result for  5  * factorial( 4 ):  120
120
```
## Program control using if,elif,else 
* Unlike every other programming language I've used before, Python does not have a switch or case statement.
* Therefore we will using if, elif condition to full fill this requirements

### Example 
```
import sys
print("1. Addition")
print("2. Subtrtaction")
print("3. Multiplication")
print("4. Division")
print("5 Exit")
n=int(input("Enter Your Condition:"))
if (n==1):
    num1=int(input("Enter your first number :"))
    num2=int(input("Enter your second number :"))
    print("Addition:",num1+num2)
            
elif (n==2):
    num1=int(input("Enter your first number :"))
    num2=int(input("Enter your second number :"))
    print("Subtraction:",num1-num2)

elif (n==3):      
    num1=int(input("Enter your first number :"))
    num2=int(input("Enter your second number :"))
    print("Multiplication:",num1*num2)

elif (n==4):
    num1=int(input("Enter your first number :"))
    num2=int(input("Enter your second number :"))
    print("Division:",num1/num2)
    
elif (n==5):
    sys.exit()
    
else:
    print("Wrong Input")
    
```
Output
```
1. Addition
2. Subtrtaction
3. Multiplication
4. Division
5 Exit
Enter Your Condition:1
Enter your first number :12
Enter your second number :12
Addition: 24
```
## Array and its type
* An array is a collection of elements of the same type.
* Creating an array in python will need a module called array.
### Example
```
inmport array as arr
a=arr.array('d',[1.1,3.5,4.5])
print(a)
```
* Here, we created an array of float type. The letter 'd' is a type code. 
* This determines the type of the array during creation.
##### _Commonly used Types codes:_
```
Code 	C Type      	Python Type 	Min bytes
'b' 	signed char 	    int 	       1
'B' 	unsigned char 	    int 	       1
'u' 	Py_UNICODE  	   Unicode 	       2
'h' 	signed short 	     int 	       2
'H' 	unsigned short 	     int 	       2
'i' 	signed int           int 	       2
'I' 	unsigned int 	     int 	       2
'l' 	signed long 	     int 	       4
'L' 	unsigned long 	     int 	       4
'f' 	float 	            float 	       4
'd' 	double 	            float 	       8
```
### Accessing array elements 
We can access a  range of items in an array by using the slicing operator :
```
    import array as arr
    numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
    numbers_array = arr.array('i', numbers_list)
    print(numbers_array[2:5]) # 3rd to 5th
    print(numbers_array[:-5]) # beginning to 4th
    print(numbers_array[5:])  # 6th to end
    print(numbers_array[:])   # beginning to end
```
Output
```
array('i', [62, 5, 42])
array('i', [2, 5, 62])
array('i', [52, 48, 5])
array('i', [2, 5, 62, 5, 42, 52, 48, 5])
```
### Changing or Adding elements 
Arrays are mutable; their elements can be changed in a similar way like lists.
```
import array as arr
numbers=arr.array('i',[1,1,3,5,7,10])
numbers[0]=0
print(numbers)
numbers[2:5]=arr.array('i',[1,2,3])
print(numbers)
```
Output:
```
array('i', [0, 1, 3, 5, 7, 10])
array('i', [0, 1, 1, 2, 3, 10])
```
We can add one item to a list using the append() method, or add several items using extend() method.
```
import array as arr
num=arr.array('i',[1,2,3])

num.append(4)
print(num)

num.extend([5,6,7])
print(num)
```
Output:
```
array('i', [1, 2, 3, 4])
array('i', [1, 2, 3, 4, 5, 6, 7])
```
We can concatenate two arrays using + operator.
```
import array as arr
odd=arr.array('i',[1,3,5])
even=arr.array('i',[2,4,6])

numbers=arr.array('i')
numbers=odd+even

print(numbers)
```
Output:
```
array('i', [1, 3, 5, 2, 4, 6])
```
### Remove/Delete
We can delete one or more items from an array using Python's del statement.
```
import array as arr
num=arr.array('i',[1,2,3,3,4])
del number[2]
print(num)
```
Output:
```
array('i', [1, 2, 3, 4])
```
We can use the remove() method to remove the given item, and pop() method to remove an item at the given index.
```
import array as arr
num=arr.array('i',[10,11,12,13])

num.remove(12)
print(num)

print(num.pop(2))
```
Output:
```
array('i', [10, 11, 13])
13
```
## Python | Using 2D arrays
* Python provides many ways to create 2-Dimensional arrays.
* However one must know the differences between these ways because they can create complications in code that can be very difficult to trace out.
* Lets start by looking at common ways of creating 1d array of size N initialized withs 0s.
#### _Method 1a_
```
import array as arr
N=5
arr=[0]*N
print(arr)
```
Output:
```
[0, 0, 0, 0, 0]
```
Extending the above we can define 2-dimensional arrays in the following ways.
```
import array as arr
rows,cols=(5,5)
arr=[[1]*cols]*rows
print(arr)
```
Output:
```
[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
```
### Example
```
two=[[1,2],[4,5],[6,7]]
for i in range(len(two)):
	for j in two[i]:
		print(j,end=" ")
	print() 
```
Output:
```
1 2 
4 5 
6 7
```
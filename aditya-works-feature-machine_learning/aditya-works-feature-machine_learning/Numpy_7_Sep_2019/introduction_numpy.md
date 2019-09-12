
### What is numpy ? 

Numpy is a library consisting of multidimensional array objects and a collection of routines 
for processing those arrays.
Using numpy we can performed locical and mathematicals operations
Numpy array class is called ndarray


Numpy array class is called ndarray.
It is also known by the alias array.

Numpy.array is not the same as the standard python libarary class array.array
which only handles one-dimensional array and offer less functionality.

ndarray.ndmin
the number of axes(dimensions) of the array.
ndarray.shape
the dimesions of the array. This is a tupple of integer indicating the size of the 
array in each dimension.
ndarray.size
the total number of elements of the array. This is equal to the product of the elements
of shape.
ndarray.dtype
an object decribing the type of the elements in the array.
ndarray.itemsize
the size in bytes of each element of the array.
ndarray.data
the buffer containing the actual elements of the array.

#### Importing numpy 


```python
import numpy as np
```


```python
# Creating a numpy varaible 
a = np.arange(15).reshape(3,5)
print(a)
```


```python
# This will show the shape of the array
print(a.shape)
```


```python
# This will show the dimension of the array
a.ndim
```


```python
# Object describing the type of the elements in the array
a.dtype.name
```


```python
#The size in the bytes of each element of the array
a.itemsize
```


```python
# Total number of elements in the array 
a.size
```

#### Array Creation

There are several ways to create arrays.
You can create an array from a regular python list or tuple using the array function.
The type of the resulting array is deduced from the type of the type of the elements in the sequences.


```python
import numpy as np
a = np.array([2,3,4])
print(a)
print(a.dtype)
b = np.array([1.2,3.5,5.1])
print(b.dtype)
```

A frequent error consists in calling array with multiple numeric arguments, rather than providing a
single list of numbers as an argument


```python
a = np.array(1,2,3,4) # WRONG
a = np.array([1,2,3,4]) # RIGHT
```

Array transforms sequences of sequences into two-dimensional array


```python
b = np.array([(1.5,2,3),(4,5,6)])
print(b)
```

The type of the array can also be explicitly specified at creation time:


```python
c = np.array([[1,2],[3,4]], dtype = complex)
print(c)
```

The function zeros creates an array full of zeros, the function ones creates an array full of ones,
and the function empty creates an array whose initital content is random and depends on the state 
of the memory.


```python
np.zeros((3,4))
```


```python
np.ones((2,3,4), dtype = np.int16 )
```

#### Data Type Objects (dtype)

A data type object describes interpretation of fixed block of memory corresponding to an array,depending on the fiollowing aspects
* Type of data(integer, float or python object)
* Size of data
* Byte Order 
* In case of structured type the names of fields, data type of each field and part of the memory block 
taken by each field
* if data type is a subarray, its shape and data type

##### Example 1


```python
# using array-scalar type
import numpy as np
dt = np.dtype(np.int32)
print(dt)
```

    int32
    

#### Example 2


```python
# int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc.
import numpy as np
dt = np.dtype('i4')
print(dt)
```

    int32
    

#### Example 3


```python
# first create structured data type 
import numpy as np
dt = np.dtype([('age',np.int8)])
print(dt)
```

    [('age', 'i1')]
    


```python
# now apply it to ndarray object 
import numpy as np
dt = np.dtype([('age',np.int8)])
a = np.array([10,20,30],dtype = dt)
print(a['age'])
```

    [10 20 30]
    

#### Example 7
The following example define a structured data type called student with a string field 'name', an integer field 'age' and a float field 'marks'. This dtype is applied to ndarray object.


```python
import numpy as np
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
print(student)
```

    [('name', 'S20'), ('age', 'i1'), ('marks', '<f4')]
    

### ndarray.shape
This array attribute returns a tuple consisting of array dimensions.It can also be used to resize the array.

#### Example 1


```python
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
```

#### Example 2 


```python
# this resize the ndarray 
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
a.shape= (3,2)
print(a)
```

    [[1 2]
     [3 4]
     [5 6]]
    

#### Example 3 


```python
# The same function that has been show above can be done as follows : 
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print("Before reshape : ")
print(a)
print("After reshape : ")
print(b)
```

    Before reshape : 
    [[1 2 3]
     [4 5 6]]
    After reshape : 
    [[1 2]
     [3 4]
     [5 6]]
    

### ndarray.ndim
This array attribute returns the number of array dimensions.


#### Example 1


```python
# an array of evenly spaced number 
import numpy as np
a = np.arange(24)
print(a)
```

    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
    

#### Example 2


```python
# this is one dimensional array
import numpy as np
a = np.arange(24)
a.ndim
# Reshaping it.
b = a.reshape(2,4,3)
print(b)
# b is having three dimensions

```

    [[[ 0  1  2]
      [ 3  4  5]
      [ 6  7  8]
      [ 9 10 11]]
    
     [[12 13 14]
      [15 16 17]
      [18 19 20]
      [21 22 23]]]
    

#### numpy.itemsize
This array attribute the length of each element of array in bytes.

#### Example 1


```python
#dtype of array is int8 (1 byte)
import numpy as np
x = np.array([1,2,3,4,5], dtype = np.float32)
print(x.itemsize)
```

    4
    

### Numpy Zeros 
Returns a new array of specified size, filled with zeros


```python
import numpy as np
print("Without any typed defined : ")
x = np.zeros(5)
print(x)
print("With the type defined : ")
x = np.zeros(5, dtype = np.int)
print(x)
print("Custom typed ")
x = np.zeros((2,2), dtype = [('x','i4'),('y','i4')])
print(x)

```

    Without any typed defined : 
    [0. 0. 0. 0. 0.]
    With the type defined : 
    [0 0 0 0 0]
    Custom typed 
    [[(0, 0) (0, 0)]
     [(0, 0) (0, 0)]]
    

### Numpy One
Returns a new array of specified size and type , filled with ones.


```python
import numpy as np
print("Without any typed defined : ")
x = np.ones(5)
print(x)
print("With type : ")
x = np.ones([2,2], dtype = int)
print(x)
```

    Without any typed defined : 
    [1. 1. 1. 1. 1.]
    With type : 
    [[1 1]
     [1 1]]
    

#### nupmpy.asarray
This function is similar to numpy.array expect for the fact that it has fewer parameter. This routine is
useful for converting. Python sequence into ndarray.


```python
import numpy as np
x = [1,2,3]
print("Converting the list to ndarray ")
a = np.asarray(x)
print(a)

x = [1,2,3]
print("dtype is set ")
a = np.asarray(x, dtype = float)
print(a)

print("ndarray from tuple")
x = (1,2,3)
a = np.asarray(x)
print(a)
```

    Converting the list to ndarray 
    [1 2 3]
    dtype is set 
    [1. 2. 3.]
    ndarray from tuple
    [1 2 3]
    

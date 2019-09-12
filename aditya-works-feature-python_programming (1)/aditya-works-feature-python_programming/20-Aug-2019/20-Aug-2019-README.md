### Below Code Description

1. Imported all the module like 
```
import os
To perform operation on directories
```

```
import collections
To check the duplicate value from a list
```

```
import hashlib
To create a md5 hash for each file
```
2. Creating a Class to have a object oriented approach 
and have an advantage to reuse the variables and methods.

3. Create Three methods name show_duplicate, 
show_checksum and remove_duplicate

##### Show_duplicate 
```
In this function we firstly ask user for
a root directory, Using this root directory 
we traverse the sub-directories.

We have use os.walk function which will discover 
all the possible directories using a for loop.

Storing all the file name in a list using append method.

Here the duplicate is a list in which duplicate file name 
has been stored using collection counter method.

Then printing the duplicate values using a loop. 

```
#### Show_checksum
```
In this function we firstly ask user for
a root directory, Using this root directory 
we traverse the sub-directories.

We have use os.walk function which will discover 
all the possible directories using a for loop.

Storing all the file name in a list using append method.

Using this templist we create another list in which the generated
checksum has been stored.

We have created checksum using hashlib.md5 method
and for showing in a well formed manner.

I had created a dictionary of filename with there respected checksum. 
```

#### Remove_duplicate
```
In this function we firstly ask user for
a root directory, Using this root directory 
we traverse the sub-directories.

We have use os.walk function which will discover 
all the possible directories using a for loop.

Storing all the file name along with is path in a list using append method.

Creating another list where all the duplicate file name has been 
stored.

Using the fullpath and the duplicate list we created a dictionary

Using this dictionary values we remove the file using
os.remove method.
```

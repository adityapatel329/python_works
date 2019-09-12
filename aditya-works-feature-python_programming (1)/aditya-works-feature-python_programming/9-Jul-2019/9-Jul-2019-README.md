## File Handling in Python

### What is a file ?
* File is a named location on disk to store related information.
* It is used to permanently store data in a non-volatile memory.
* Since,random access memory (RAM) is volatile which loses its data when
computer is off, we use files for future use of the data.
* When we want to read from or write a file we need to open it first.
* When we are done, it needs to be closed, so that resources that are tied with the file are freed.

Hence, in Python, a file operation takes place in the following order.

1. Open a file 
2. Read or write(perform operation)
3. Close the file 

### Opening a file 
* Python has a built-in function open() to open a file.
* This function returns a file object, also called a handle, as it is used to read or modify accordingly.
```
    f=open("test.txt")
    f=open("C:/Python33/README.txt")
```
* We can specify the mode while opening a file.
* In mode, we specify whether we want to read 'r', write 'w' or
append 'a' to the file.
* We also specify if we want to open the file in text mode or binary mode.
* The default is reading in text mode.In this mode,we get strings when reading from the file.
* On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non-text files like 
images or exe files.

```
Mode                Description
'r'	       Open a file for reading. (default)
'w'	       Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	       Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	       Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	       Open in text mode. (default)
'b'	       Open in binary mode.
'+'	       Open a file for updating (reading and writing)
```
#### Example
```
f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode 
f = open("img.jpg",'r+b') # read and write in binary mode 
```
* Moreover, the default encoding is platform dependent.
* In windows, it is 'cp1252' but 'utf-8' in Linux.
* So, we must not also rely on the default encoding or else our code will behave differently in differently in different platforms.
* Hence, when working with files in text mode, it is highly recommended to specify the encoding type.
```
f = open("test.txt",mode = 'r',encoding = 'utf-8')
```
### Closing a file
* When e are done with operations to the file.
* Closing a file will free up the resources that were tied with the file and is done using Python close() method.
* Python has a garbage collector to clean up unreferenced objects but, we must not rely on it to close the file.
```
f = open("test.txt",encoding = 'utf-8')
# perform file operations
f.close()
```
This method is not entirely safe.if an exception occurs when we are performing some operation with the file,
the code exists without closing the file.
A safer way is to use a try and finally block.
```
try:
    f =open("test.txt",encoding = 'utf-8')
    # perform file operations
finally:
    f.close()   
```
* This way, we are guaranteed that the file is properly close even if an exception is raised,
causing program flow to stop.

* The best way to do this is using the "with" statement.
* We don't need to explicitly call the close() method.
```
with open("test.txt",encoding = 'utf-8') as f:
    # perform file operations
``` 
### Writing a file in python
* In order to write into a file in python, we need to open it in write 'w' ,
append 'a' or exclusive creation 'x' mode.
* We need to be careful with the 'w' mode as it will overwrite into the file if it already exists.
#### Example 
```
with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
```
This program will create a new file named 'test.txt'

### Reading a file in python
* To read a file in Python, we must open the file in reading mode.
* There are various methods available for this purpose.
* We can use the read(size) method to read in size number of data.
* If size parameter is not specified, it reads and returns up to the end of the file.
```
f = open("test.txt",'r')
f.read(4)
'This' #reading the first 4 data

f.read(4) # it includes white space
' is '
```
* We can see that, the read() method returns newline as '\n'. Once the end of file is reached, we get empty string on further reading

```
f.tell() # can get the current position
56

f.seek(0) # bring file cursor to initial position
0 
```
* Reading a file line-by-line using a for loop.
* This is both efficient and fast.
```
f=open("test.txt")
for line in f:
    print(line , end = '')
```
Output:
```
This is my first file
This file 
contains three lines
```
We can use readline() method to read individual line of a file. This method reads a file till
the newline, including the newline character.
```
f=open("test.txt")
f.readline()
```
Output:
```
'This is my first file\n'
```
## Python file Manipulation methods
```
Method	                    Description
close()            Close an open file.
detach()           Separate the underlying binary buffer.
fileno()           Return an integer number of the file.
flush()            Flush the write buffer of the file stream.
isatty()           Returns "True" if the file stream is interactive.
read(n)            Read atmost n character from the file.
readable()         Returns "True" if the file stream can be read from.
readline(n=-1)     Read and return a list of lines from the file.
tell()             Returns the current file location.
write(s)           Write string s to the file and return the number of characters written.
        

```
### How to Run the program
```
>> python main.py -o read -fn input.txt
    To read the file 
 
>> python main.py -o write -fn input1.txt -wn "My name is aditya"
    write successful #will print
    
>>> python main.py -o nlines -fn input.txt
1. FirstLine
2. LastLine
Enter which line to find 1
My name is aditya 


>>> python main.py -o copy -fn input.txt -on output.txt
  Data copied succesfully   



>>> python main.py -o re_name
9-Jul-2019-README .md
input .txt
main .py
output .txt
choice which file to be renamed : input.txt
Type a new name : input1.txt

rename successfully

9-Jul-2019-README .md
input1 .txt
main .py
output .txt

>python main.py -o delete_file
9-Jul-2019-README .md
input1 .txt
main .py
output .txt
Choice a file to be deleted : output.txt
Delete successfully
  
```
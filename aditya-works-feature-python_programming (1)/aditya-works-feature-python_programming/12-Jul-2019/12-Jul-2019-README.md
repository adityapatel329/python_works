## Python Multiprocessing 
* Parallel processing is getting more attention nowadays.
* As Creating parallel code is a great way to improve performance.
* Python introduced multiprocessing module to let us write parallel code.
* There are plenty of classes in python multiprocessing module for building
a parallel program.
#### _Three basic classes in python multiprocessing are_
1. Process
2. Queue
3. Lock
* To make a parallel program useful, you have to know how many cores are there
in you pc
* The following code will print the number of cores in yours pc.
```
import multiprocessing 
print("Number of cpu : ",multiprocessing.cpu_count())
```
Output
```
Number of cpu : 4
```
### Python multiprocessing Process class
* Python multiprocessing Process class is an abstraction that sets up another
Python process, provides it to run code and a way for the parent application to control
execution.
* There are two important functions that belongs the Process class 
* start() and join() function.
* At first, we need to write a function, that will be run by the process
* Then we need to instantiate a process object.
* if we create a process object, nothing will happen until we tell it to start 
processing via start() function.
* Then, the process will run and returns its result. 
* After that we tell the process to complete via join() function.
* Without join() function call, process will remain idle and won't terminate 
* So if you create many processes and don't terminate them, you may face 
scarcity of resources.
```
from multiprocessing import Process
from time import sleep
def calc_square(numbers):
    for n in numbers:
        sleep(5)
        print("square "+str(n*n))

def calc_cube(numbers):
    for n in numbers:
        sleep(5)
        print("cube "+ str(n*n*n))
    
if __name__ == "__main__":
    arr=[2,3,8,9]
    p1 = Process(target=calc_square, args=(arr,))
    p2 = Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")

```
Output:
```
square 4
cube 8
square 9
cube 27
square 64
cube 512
square 81
cube 729
Done!
```
* Every process has its own address space(virtual memory). 
* Thus program variables are not shared between two process.
* You need to use inter-processes  techniques if you want to share data between 
processes
## Python multiprocessing queue class
* Python multiprocessing modules proves Queue Class 
that is exactly a First-In-First-Out data structure.
* They can store any pickle Python object.
* Queue are specially useful when passed as parameter to a Process
target function to enable the Process to consume data.
* By using put() function we can insert data to then queue and
using get() we can get items from queue.
* See the following code for a quick example.
```
from multiprocessing import *
def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n)

if __name__ == "__main__":

    numbers=[2,3,5]
    q=Queue()
    p=Process(target=calc_square,args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())
```
Output:
```
4
9
25
```
#### Multiprocessing Queue vs Queue Module
import multiprocessing 
q = multiprocessing.Queue()
 * Lives in shared memory
 * Used to share data between process
 import queue
 q = queue.Queue()
 * Lives in in-process memory
 * used to share data between threads
## Python multiprocessing Lock Class
* The tasks of class is quite simple.
* It allows code to claim lock so that no other process can execute 
the similar coed until the lock has been released.
* So the task of Lock class is mainly two.
* One is to claim lock and other is to release the lock.
* To claim lock, acquire() function is used and to release lock release() function
is used.
* Suppose we have some tasks to accomplish.
* To get that task done, we will use several process.
* So we don't need to use the Lock class to block multiple process
to access the same object.
```
import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        #time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value +1
        lock.release()

def withdraw(balance, lock):
    for i in range(100):
        #time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i',200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args=(balance,lock))
    w = multiprocessing.Process(target=withdraw, args=(balance,lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)
```
Output:
```
200
```
## Multithreading in python
* In computing, a process is an instance of a computer program
that is being executed.
* Any process has 3 basic components:
1. An executable program.
2. The associated data needed by the program
3. The execution context of the program
* A thread is an entity within a process that can be scheduled for execution.
* Also, it is the smallest unit of processing that can be performed in an OS.
* In simple words, a thread is a sequence of such instruction within a program 
* For simplicity, you can assume that a thread a thread is simply a subset of a process
* A thread contains all this information in a Thread Control Block(TCG):
1. Thread Identifier : Unique id (TID) is assigned to every new thread
2. Stack Pointer : Points to thread's stack in the process. Stacks contains the local
variables under thread scope.
3. Program counter : A register which stores the address of the instruction
currently being executed by thread.
4. Thread state : Register assigned to thread for computations.
5. Parent process Pointer : A pointer to the process control block (PCB)
of the process that the thread lives on.
### Example:
```
import time
import threading

def calc_square(numbers):
    print("Calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square : ',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube : ',n*n*n)

arr = [2,3,8,9]

t=time.time()

t1 = threading.Thread(target = calc_square, args=(arr,))
t2 = threading.Thread(target = calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : ",time.time() - t)
print("Hah. . . I am done with all my work now!")
```
Output:
```
Calculate square numbers
calculate cube of numbers
square :  4
cube :  8
square :  9
cube :  27
square :  64
cube :  512
square :  81
cube :  729
done in :  0.8059289455413818
Hah. . . I am done with all my work now!
```
## Python Global Interpreter Lock (GIL)
* The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter.
* This means that only one thread can be in a state of execution at any point in time.
* The impact of the the GIL isn't visible to developers who execute single-threaded programs, but it can be performance bottleneck in CPU-bound and multi-threaded code.
* Python uses reference counting for memory management.
* It means that objects created in Python have reference count variable that keeps track of the number of references that 
point to the object. 
* When this count reaches zero, the memory occupied by the object is released.
```
import sys
a = []
b = a
sys.getrefcount(a)
```
* The problem was that this reference count variable needed protection from race conditions where two threads increase or decrease its value simultaneously.
* If this happens, it can cause either leaked memory that is never released or, even worse, incorrectly release the memory while a reference to that object still exists.
* This can cause crashes or other "weired" bugs in your python programs.
#### _Deal with python's GIL_
* if the GIL is causing you problems, here a few you can try :
* Multi-processing vs multi-threading : The most popular way is to use a 
multi=processing approach where you use multiple processes instead of threads.
* Each python process get its own python interpreter and memory space so the GIL 
won't be a problem.
* Python  has a multiprocessing module which lets us create processes early like this :
#### Pipes
* The Pipe() function returns a pair of connection objects connected by a pipe
which by default is duplex(Two-way)
* The two connections objects returned by Pipe() represent the two ends of the pipe.
* Each connection object has send() and recv() methods.
* Note that data in a pipe may become corrupted if two processes try to read from 
or write to the same end of the pipe at the same time.
* Of course there is no risk of corruption from processing 
using different ends of the pipe at the same time.
## Multitasking in python
* Modern operating systems allow a user to run several applications simultaneously, so that some tasks can be run in the background while the user continues with other work in the foreground.
* To create a task we can use process or thread.
* Process has its private resources including memory mapping, files and other os objects. 
* Multiple threads can run on the same process and share all its resources but if one thread fail it will kill all other threads in its process.
##### _Python has many packages to handle multi tasking and they are as follow:_
1. os.fork
- Unix/Linus/OS X specific. The function creates a child process that start
running after the fork return.
- We call fork once but it returns twice on the parent and on the child.
- Consider the following code:
```
import os
x = os.fork()
if x:
    print('hello parent')
else:
    print('hello child')
```
Output:
```
hello parent
hello child
```
2. os.system
* Runs a command in the shell sometimes you only need
to run another program or command.
* For example you want to do something that easily done with a command like format.
```
import os
status = os.system('script2.py')
print("exit status",status)
```



 

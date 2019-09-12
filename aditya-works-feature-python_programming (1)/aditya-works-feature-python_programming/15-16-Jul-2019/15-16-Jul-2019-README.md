## Thread Synchronization
* Thread synchronization is defined as a mechanism which ensures
that two or more concurrent thread do not simultaneously execute some particular
program known as critical section.
* Critical section refers to the parts of the program where the shared 
resources is accessed. 
* Concurrent accesses to shared resources can lead to race condition.
* A race condition occurs when two or more threads can access shared data 
and they try to change it at the same time.
* As a result, the values of variables may be unpredictable and vary
depending on the timings of context switches of the process.

[Race Condition Example](C:\Users\Public\Downloads\aditya-works\15-16-Jul-2019\race_conditionexamples)
* In above program 
* Two threads t1 and t2 are created in main_task function and global variable 
x is set to 0.
* Each thread has a target function thread_task in which increment function is called
100000 times.
* Increment function will increment the global variable x by 1 in each call.
* The expected final value of x is 2000000 but what we get in 10 iterations of main_task
function is some different values.
* This happens due to concurrent access of threads to the shared variable x.
* This unpredictability in value of x is nothing but race condition.
* Given below is a diagram which shows how can race condition occur in 
above program:

#### _Hence, we need a tool for proper synchronization between multiple-threads_
1.Using Locks
*  Threading module provide a Lock class to deal with the race condition.
#### _Lock class provides following methods:_
1.1 :- acquire([blocking]):To acquire a lock. A lock can be blocking or non-blocking.
* When invoked with the blocking argument set to True (the default), thread execution is blocked until the lock is unlocked, then lock is set to locked and return True.
* When invoked with the blocking argument set to False, thread execution is not blocked. If lock is unlocked, then set it to locked and return True else return False immediately.\

1.2 :- release() : To release a lock.
* When the lock is locked, reset it to unlocked and return.
* if any another threads are blocked waiting for the lock to become unlocked
allow exactly one of them to proceed.
* if lock is already unlocked, a ThreadError is raised.

[Lock Condition Example](C:\Users\Public\Downloads\aditya-works\15-16-Jul-2019\race_condition_examples)

Let us try to understand the above code step by step:
* Firstly,a Lock object us created using:\
``
lock = threading.Lock()
``
* Then,lock is passed as target function argument:\
```
  t1 = threading.Thread(target=thread_task, args=(lock,))
  t2 = threading.Thread(target=thread_task, args=(lock,))
```
* In the critical section of target function, we apply lock using lock.acquire() method. As soon as a lock is acquired, no other thread can access the critical section (here, increment function) until the lock is released using lock.release() method.
```
  lock.acquire()
  increment()
  lock.release()
```
* As you can see in the results, the final value of x comes out to be 200000 every time (which is the expected final result).

####  _Here are the few Advantages and Disadvantages of Multithreading_
#### Advantages:
1. It doesn’t block the user. This is because threads are independent of each other.
2. Better use of system resources is possible since threads execute tasks parallely.
3. Enhanced performance on multi-processor machines.
4. Multi-threaded servers and interactive GUIs use multithreading exclusively.
#### Disadvantages:
1. As number of threads increase, complexity increases.
2. Synchronization of shared resources (objects, data) is necessary.
3. It is difficult to debug, result is sometimes unpredictable.
4. Potential deadlocks which leads to starvation, i.e. some threads may not be served with a bad design
5. Constructing and synchronizing threads is CPU/memory intensive.

## Multi Thread VS Single Thread :
| Index   |      Multithreading      |  Simple Treading |
|----------|:-------------:|:---------:|
|  1  |  Multiple Thread run at the same time | Single thread run at the same time  |
|  2  |    Cpu time is never wasted  | Cpu time is wasted  |
|  3  | Idle time is minimum |  Idle time is maximum |
|  4  | More Efficient  | Less Efficient |
|  5  | Execution time is fast |   Execution time is slow |

## Parallel processing in python using pool class :
* This class represents a pool of worker processes; its methods let us offload tasks to such processes. Let’s take an example (Make a module out of this and run it).
* We create an instance of Pool and have it create a 3-worker process. map() maps the function double and an iterable to each process. The result gives us [4,6,12].
* Another method that gets us the result of our processes in a pool is the apply_async() method.






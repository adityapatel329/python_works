#### _Memory Management_
* Everything in Python is an object. Some objects can hold other objects, such as lists, tuples, dicts, classes, etc.
* Because of dynamic Python's nature, such approach requires a lot of small memory allocations. 
* Python's memory allocation and deallocation method is automatic.
* Python uses two strategies for memory allocation reference counting and garbage collection.
* Python interpreter only used reference counting for memory management.
* Reference counting works by counting the number of times an object is referenced by other objects in the system.
* When references to an object are removed, the reference count for an object is decremented.
*  When the reference count becomes zero the object is deallocated.

#### _The easiest way to create a reference cycle is to create an object which refers to itself as in the example below:_
```
def make_cycle():
    1 = [ ]
    1.append(l)

make_cycle()
```
Because make_cycle() creates an object 1 which refers to itself, the object 1 will not automatically be freed when the function returns.
#### _Automatic garbage collection of cycles_
* Python schedules garbage collection based upon a threshold of object allocations and object deallocations.
* When the number of allocations minus the number of deallocations are greater than the threshold number, the garbage collector is run.
#### _Example:_
```
import gc
print "Garbage collection thresholds: %r" % gc.get_threshold()

Garbage collection thresholds: (700, 10, 10)
```
Here we can see that the default threshold on the above system is 700.\
This means when the number of allocations vs. the number of deallocations is greater than 700 the automatic garbage collector will run.

#### _Python memory management is been divided into two parts._
1. Heap Memory
2. Stack Memory
* Methods and variables are created in Stack memory.
* Objects and instance variables values are created in Heap memory.
* In stack memory - a stack frame is created whenever methods and variables are created.
* These stacks frames are destroyed automaticaly whenever functions/methods returns. 
#### _Process of storing objects_

[Imgur](https://i.imgur.com/YWPmlEp.jpg)
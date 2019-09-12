## Duck Typing in Python

### Dynamic Typing
* Python is dynamically but strongly typed. The fact that the two halves of that statement fit together can confuse those who come from a static language type background. In Python it is perfectly legal to do this :
```
variable = 3
variable = 'hello'
```
* So hasn't variable just changed type ?
*  The answer is a resounding no. variable isn't an object at all - it's a name
* In the first statement we create an integer object with the value 3 and bind the name 'variable' to it.
*  In the second statement we create a new string object with the value hello, and rebind the name 'variable' to it.
* If there are no other names bound to the first object (or more properly no references to the object - not all references are names) then it's reference count will drop to zero and it will be garbage collected.

### Duck Typing 
* There is another concept in this typing lark that is a feature of dynamic languages. This is duck Typing.
* The idea is that it doesn't actually matter what type my data is - just whether or not I can do what I want with it.
* For example in a statically typed language we have a concept of adding.
* Some types of object can be added - usually only to object of the same type.
* In python we allow the object to define what it means to be added.
* The expression 3 + 3 is syntactic sugar for calling 
the __add__ method of integer type.
* It's the same as calling init.__add__(3, 3): 
* This means that if you define an __add__ method for one 
of your classes you can make all sorts off things happen when you add instances
of them together
```
a = [0,1 2, 3]
print a[0]
0

b = {'a': 0, 'b': 1}
print b['a']
0
```
is exactly the same as :
```
a =  [0,1 2, 3]
print list.__getitem__(a, 0)
0

b = {'a': 0, 'b': 1}
print dict._getitem__(b, 'a')
0
```
* In first example we use normal python syntax.
* In the second example we do what the first example is doing.
* In order to set members we would use the __setitem__ method instead of __getitem__.
* There are lots more examples of syntactic sugar - including comparing objects and accessing
attributes.
* Duck typing happens because when we do a['member'] Python doesn't care what type object a is.
* All it cares is whether the call it's __getitem__ method returns anything sensible.
## Decorators in Python
 * In Python, functions are the first class objects, which means that –
 * Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
 * Functions can be defined inside another function and can also be passed as argument to another function.
 #### Decorators
 * Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
 *  Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
 * In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
 ```
 @gfg_decorator
def hello_decorator(): 
    print("Gfg") 
  
'''Above code is equivalent to - 
  
def hello_decorator(): 
    print("Gfg") 
      
hello_decorator = gfg_decorator(hello_decorator)'''
 ```
* In the above code, gfg_decorator is a callable function, will add some code on the top of some another callable function, hello_decorator function and return the wrapper function.

 
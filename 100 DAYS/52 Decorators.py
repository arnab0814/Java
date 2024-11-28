'''Python Decorators'''

# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:
'''
@decorator_function
def my_function():
    pass
'''
# The @decorator_function notation is just a shorthand for the following code:
'''
def my_function():
    pass
my_function = decorator_function(my_function)
'''
# Decorators are often used to add functionality to functions and methods, such as logging, memoization, and access control.



'''Practical use case'''
# One common use of decorators is to add logging to a function. For example, you could use a decorator to log the arguments and return value of a function each time it is called:
'''
import logging
def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated
@log_function_call
def my_function(a, b):
    return a + b
'''
# In this example, the log_function_call decorator takes a function as an argument and returns a new function that logs the function call before and after the original function is called.


'''Conclusion'''
# Decorators are a powerful and flexible feature in Python that can be used to add functionality to functions and methods without modifying their source code. They are a great tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.

# In conclusion, python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code. They are used for a variety of purposes, such as logging, memoization, access control, and more. They are a powerful tool that can be used to make your code more readable, maintainable, and extendable.


# CODE



# def greet(fx):
#   def mfx(*args, **kwargs):
#     print("Good Morning")
#     fx(*args, **kwargs)
#     print("Thanks for using this function")
#   return mfx

# @greet
# def hello():
#   print("Hello world")

# @greet
# def add(a, b):
#   print(a+b)
  
# # greet(hello)()
# hello()
# # greet(add)(1, 2)
# add(1, 2)


# MY CODE

# here the (func) is the fucntion which we want to modify, here we only take a function name not a arguments of the function which we want to modify
def user_decorator(func):
# this decorator function returns a local function, since it takes a function, this local function contains all the required modification
    def decorated():
        print("Hii user your output is :-")
        func()   # here is the fucntion that what we want to modify
        print("Have a good day")
    
    return decorated

# to use decorator on a particular function, then we have to call it just before the fucntion is build, the decorator can be called by the @ code
@user_decorator
def just_func():
    print("Function has been modified")
# once the function is completed with the decorator then we can call our funciton normally 
# just_func()
# the function will be modifiy 

# ----------------------------------------------------------------------------------------------------------------------------------------


# to pass argumetns with function we use *args and *kargs method in the local function of the decorator
def user_decorator(func):
    def decorated(*args, **kwargs):
        # just we use args and kwargs here to pass the arguments of the function
        print("Hii user your output is :-")
        func(*args, **kwargs)
        print("Have a good day")
    
    return decorated


@user_decorator
def addd(a,b):
    print(a+b)


# addd(4,5)


# ----------------------------------------------------------------------------------------------------------------------------------------

# NOTE:- we can use a single *args or ** kwargs method
def user_decorator(func):
    def decorated(*args):
        # just we use args and kwargs here to pass the arguments of the function
        print("Hii user your output is :-")
        func(*args)
        print("Have a good day")
    
    return decorated


@user_decorator
def addd(a,b,c,d):
    print(f"a={a},b={b},c={c},d={d}")

# addd(4,5,6,7)

# ----------------------------------------------------------------------------------------------------------------------------------------

# NOTE:- also we can use a normal parameters
def user_decorator(func):
    def decorated(arg):
        # just we use args and kwargs here to pass the arguments of the function
        print("Hii user your output is :-")
        func(arg)
        print("Have a good day")
    
    return decorated


@user_decorator
def addd(a):
    print(f"a={a}")


addd(4)
'''Magic/Dunder Methods in Python'''

# NOTE:- THIS THINGS ARE ONLY WORK WITH THE OBJECTS 


## These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour.

# Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes. They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.

'''Some of the most commonly used magic methods in Python.'''

'''__init__ method'''
# The init method is a special method that is automatically invoked when you create a new instance of a class. This method is responsible for setting up the object’s initial state, and it is where you would typically define any instance variables that you need. Also called "constructor"

'''__str__ and __repr__ methods'''
# The str and repr methods are both used to convert an object to a string representation. The str method is used when you want to print out an object, while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.

'''__len__ method'''
# The len method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.

'''__call__ method'''
# The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called. This is an incredibly powerful tool that allows you to create objects that behave like functions.

# These are just a few of the many magic methods available in Python. They are incredibly powerful tools that allow you to customize the behaviour of your objects, and can make your code much cleaner and easier to understand. So if you’re looking for a way to take your Python code to the next level, take some time to learn about these magic methods.


# CODE 

class Employee:

  def __init__(self, name):
    self.name = name

  def __len__(self):
    i = 0
    for c in self.name:
      i = i + 1
    return i

  def __str__(self):
    return f"The name of the employee is {self.name} str"
    
  def __repr__(self):
    return f"Employee('{self.name}')"

#   def __call__(self):
#     print("Hey I am good")



e = Employee("Harry")

# print(str(e))
# print(repr(e))
# print(e.name)
# print(len(e))
# e()


# MY CODE
from typing import Any  # THIS WILL IMPORT DIRECTLY WHEN WE MAKE A CALL METHOD

class Base:
    def __init__(self,name) -> None:
      self.name = name
    
    # this 2 dunder methods should return soething
    def __str__(self) -> str:
      return f"'__str__' method is called"
  
    def __repr__(self) -> str:
      return f"'__repr__' method is called"
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
      print(f"this is the __call__ method")
      
    def __length__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
    
ob1 = Base("Shubham")

print(ob1.__length__())
# print(length(ob1))  harry had over ridded the len , thats why it is not giving error

ob1()
ob1.__init__("karan")   # we also update like this
print(ob1.name)      



# NOTE:- THIS THINGA CAN BE USED TO GIVE SOME KIND OF INFORMATION

print(ob1.__str__())   # we have to print since it returns
# print(str(ob1)) # same
print(ob1.__repr__())   # we have to print since it returns
# print(repr(ob1)) # same



# NOTE :- WE CAN ALSO PROVIDE CONSTRUCTOR DETAILS LIKE THIS
ob2 = Base
ob2.__init__(self=ob2,name="annu")
# NOTE :- BUT THEN WE HAVE TO PROVIDE THE (self) EVRYTIME
print(ob2.__str__(ob2))
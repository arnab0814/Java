''' ACCESS MODIFIERS '''

# Access Specifiers/Modifiers
# Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

# Let us see the each one of access specifiers in detail:

# Types of access specifiers
    # Public access modifier
    # Private access modifier
    # Protected access modifier
    
    
'''Public Access Specifier in Python'''
# All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.

# Example:
'''
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable
obj = Student(21,"Harry")
print(obj.age)
print(obj.name)
'''


'''Private Access Modifier'''
# By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.

# In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.

# Example:
'''
class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Harry")
obj1 = Subject

# calling by object of class Student
print(obj.__age)
print(obj.__funName())

# calling by object  of class Subject
print(obj1.__age)
print(obj1.__funName())
'''
# NOTE:- Private members of a class cannot be accessed or inherited outside of class. If we try to access or to inherit the properties of private members to child class (derived class). Then it will show the error.


'''Name mangling'''
# Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.
'''
class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"
my_object = MyClass()
print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute
'''
# In the example above, the attribute _nonmangled_attribute is marked as nonmangled by convention, but can still be accessed from outside the class. The attribute __mangled_attribute is private and its name is "mangled" to _MyClass__mangled_attribute, so it can't be accessed directly from outside the class, but you can access it by calling _MyClass__mangled_attribute


'''Protected Access Modifier'''
# In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.

# It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.

# Example:
'''
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())
'''


# CODE 

# class Student:
#     def __init__(self):
#         self._name = "Harry"

#     def _funName(self):      # protected method
#         return "CodeWithHarry"

# class Subject(Student):       #inherited class
#     pass

# obj = Student()
# obj1 = Subject()
# print(dir(obj))

# # calling by object of Student class
# print(obj._name)      
# print(obj._funName())     
# # calling by object of Subject class
# print(obj1._name)    
# print(obj1._funName())


# MY CODE

# PUBLIC

# class Base:
#     def __init__(self,name):
#         self.name = name
        
#     def show_detail(self):
#         print(f"Name is {self.name}")
        
    
# class Derived(Base):
#     def details(self):
#         print(f"name is {self.name}")
        
        
# ob1 = Base("shubham")
# ob2 = Derived("Karan")


# # print(ob1.name)
# # ob1.show_detail()

# ob2.name = "daya"
# ob2.show_detail()


# PRIVATE

# class Base:
#     def __init__(self,name):
#         self.__name = name
        
#     def __show_detail(self):
#         print(f"Name is {self.__name}")
        
    
# class Derived(Base):
#     def details(self):
#         print(f"name is {self.__name}")   # WE CANNOT CALL DIRECTLY INSTED INDIRECTLY
        
        
# ob1 = Base("shubham")
# ob2 = Derived("Karan")


# # print(ob1.name)
# # ob1.show_detail()

# # ob2.__name = "daya"   WE CANNOT DIRECTLY CHANGE THE VALUE 
# ob2._Base__name = "mokambo"   # BUT WE CAN CHANGE IT LIKE THIS

# # BECAUSE PYTHON RENAME IT WITH _Base NAME ONLY TO THOSE INSTANCE WHOSE NAME START FROM DOUBLE UNDERESCORE
# # print(ob2.__dir__())   # WE SEE THAT RENAME HERE ,THIS IS ONLY APPLICABLE TO THE DOUBLE UNDER SCORE NAMES
# # print(dir(ob1))


# ob2.details()   # THIS WILL GIVE ERROR WE CANNOT DIRECTLY CALL A PROTECTED INSTANCE, BUT BY INDERECTLY 


# # NOTE :- this are the ways how we can call a private instance
# # ob2._Base__show_detail()
# # ob1._Base__show_detail()



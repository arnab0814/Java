'''Python Class Methods'''

'''Python Class Methods: An Introduction'''
# In Python, classes are a way to define custom data types that can store data and define functions that can manipulate that data. One type of function that can be defined within a class is called a "method."


'''What are Python Class Methods?'''
# A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the class. Class methods are defined using the "@classmethod" decorator, followed by a function definition. The first argument of the function is always "cls," which represents the class itself.


'''Why Use Python Class Methods?'''
# Class methods are useful in several situations. For example, you might want to create a factory method that creates instances of your class in a specific way. You could define a class method that creates the instance and returns it to the caller. Another common use case is to provide alternative constructors for your class. This can be useful if you want to create instances of your class in multiple ways, but still have a consistent interface for doing so.


'''How to Use Python Class Methods'''
# To define a class method, you simply use the "@classmethod" decorator before the method definition. The first argument of the method should always be "cls," which represents the class itself. Here is an example of how to define a class method:
'''
class ExampleClass:
    @classmethod
    def factory_method(cls, argument1, argument2):
        return cls(argument1, argument2)
'''
# In this example, the "factory_method" is a class method that takes two arguments, "argument1" and "argument2." It creates a new instance of the class "ExampleClass" using the "cls" keyword, and returns the new instance to the caller.

# It's important to note that class methods cannot modify the class in any way. If you need to modify the class, you should use a class level variable instead.


'''Conclusion'''
# Python class methods are a powerful tool for defining functions that operate on the class as a whole, rather than on a specific instance of the class. They are useful for creating factory methods, alternative constructors, and other types of methods that operate at the class level. With the knowledge of how to define and use class methods, you can start writing more complex and organized code in Python.



# CODE


# class Employee:
#   company = "Apple"
#   def show(self):
#     print(f"The name is {self.name} and company is {self.company}")

#   @classmethod
#   def changeCompany(cls, newCompany):
#     cls.company = newCompany


# e1 = Employee()
# e1.name = "Harry"
# e1.show()
# e1.changeCompany("Tesla")
# e1.show()
# print(Employee.company)


# MY CODE



class Employe:
    
    company = "Samsoong"
    
    def details(self):
        print(f"the name is {self.name}, age is {self.age}, from company {self.company}")   # WE CAN ALSO DEFINE LIKE THIS AND GAIVE VALUES LATER
    
    
    # NOTE :- we have made this fuction to upadte the class variable    
    @classmethod  
    def update_class_instance(cls,newcompany):
         cls.company = newcompany
        
ob1 = Employe()
ob1.name = 'shubham'
ob1.age = 18
ob1.details()


ob2 = Employe()
ob2.name = "karan"
ob2.age = 17

# NOTE:- THIS CHANGES THE INSTANVE VALUE NOT THE CLASS VALUE, TO UPDATE THE CLASS VARIABLE WE USE @classmethod DECRORATOR 
# ob2.company = "motorola"  
# ob2.update_class_instance('motorola')  

# AFTER USING THE @classmethod DECRORATOR
# ob2.update_class_instance('motorola')  
# ob2.company = "motorola"  NOTE:- even if we use this the method, this will update only the instance no the calss variable
ob2.details()
print(Employe.company)
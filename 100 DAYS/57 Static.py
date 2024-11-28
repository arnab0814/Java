# STATIC METHOD

# Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.

# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
# result = Math.add(1, 2)
# print(result) # Output: 3

# In this example, the add method is a static method of the Math class. It takes two parameters a and b and returns their sum. The method can be called on the class itself, without the need to create an instance of the class.


# CODE 


# class Math:
#   def __init__(self, num):
#     self.num = num

#   def addtonum(self, n):
#     self.num = self.num +n
    
#   @staticmethod
#   def add(a, b):
#       return a + b

# # result = Math.add(1, 2)
# # print(result) # Output: 3
# a = Math(5)
# print(a.num)
# a.addtonum(6)
# print(a.num)

# print(Math.add(7, 2)) 


# MY CODE

class Base:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Name is {self.name}")
        
    # WHEN WE WANT TO MAKE A METHOD WICH NOT HAVE A (self) PARAMETR WE USE @staticmethod DECORATORS ,THIS ALLOWS US TO MAKE A NORMAL FUNCITON IN THE (class) 
        
    # NOTE:- WE CANT USE THE CLASS PROPERTY IN THIS STATIC METHODS, BECAUSE WE HAVE TO USE A (self) PARAMETER FOR THIS
    @staticmethod      
    def calc(a,b):
        print(f"addition is :- {a+b}")
        

ob1 = Base("Shubham")


# ONE WAY TO CALL THIS FUNCTION
ob1.show()
ob1.calc(4,5)



# NOTE:- THIS THE FINCAL WAY IN WHICH THE PYTHON CONVERTS IT WHEN THE FUCNTION CALL,SINCE HERE WE PASS AN (OBJECT) WHICH IS TAKEN BY (SELF). THE SAME THING HAPPENS THERE
# ANOTHER WAY TO CALL THIS FUCNTION
Base.show(ob1)
Base.calc(10,20)
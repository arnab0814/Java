'''Getters'''

# Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator. Here is an example of a simple class with a getter method:
'''
class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
'''
# In this example, the MyClass class has a single property, _value, which is initialized in the init method. The value method is defined as a getter using the @property decorator, and is used to return the value of the _value property.

# To use the getter, we can create an instance of the MyClass class, and then access the value property as if it were an attribute:
'''
# obj = MyClass(10)
# obj.value
'''

'''Setters'''

# It is important to note that the getters do not take any parameters and we cannot set the value through getter method.For that we need setter method which can be added by decorating method with @property_name.setter

# Here is an example of a class with both getter and setter:
'''
class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        self._value = new_value
'''
'''
# obj = MyClass(10)
# obj.value = 20
# obj.value
'''

# In conclusion, getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden. This can be useful for encapsulation and data validation.




# CODE


# class MyClass:
#   def __init__(self, value):
#       self._value = value
    
#   def show(self):
#     print(f"Value is {self._value}")
    
#   @property
#   def ten_value(self):
#       return 10* self._value
    
#   @ten_value.setter
#   def ten_value(self, new_value):
#       self._value = new_value/10

# obj = MyClass(10)
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()


# MY CODE


class Example:
    def __init__(self,value):
        self.value = value
        # value is known as property
    
    def show_value(self):
        # function is known as method
        print(f"\nThe value is {self.value}, by show_value method\n")
        
    
    @property
    # @property decorators is used to make the any method (function) a property (value,variable) , in order to use it as a property
    # and this technique is called as getter since we directly get the values
    def getter_value(self):
        print("value by getter_value :- ")
        return self.value
    
    # NOTE :- property decorators converts the whole method as property, whatever in it will get executed
    
    @getter_value.setter
    # @setter decorators as a names shows, this set the new value to the property
    def setter_value(self,new_value):
        self.value = new_value

obj = Example(10)

# NORMAL WAYS HOW WE PRINT THE VALUES
# obj.show_value()
# print(f"printing the value direct : {obj.value}\n")

# MENTOS JINDAGI
# print(obj.getter_value)  #getter



obj.setter_value = 20
# print(obj.value)
# obj.getter_value
print(obj.getter_value)
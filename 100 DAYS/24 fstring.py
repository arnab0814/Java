'''String formatting in python'''

# String formatting can be done in python using the format method.

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

'''f-strings in python'''
# It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

# When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

# Example:-
val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")


# when we want to print the content with the curly braces we can use double braces for this
print(f"the curly braces string {{20 + 20 = }}{20+20}")
'''Python Dictionaries'''

# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)


# Accessing Dictionary items:

# I. Accessing single values:
# Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name1'])            # --> NOTE:- THIS WILL GIVE ERROR IF THE KEY VALUE IS NOT THERE 
print(info.get('name1'))    # --> NOTE:- THIS WILL GIVE NONE IF THE KEY VALUE IS NOT THERE   , THIS IS THE DIFFERENCE


# II. Accessing multiple values:
# We can print all the values in the dictionary using values() method.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())


# III. Accessing keys:
# We can print all the keys in the dictionary using keys() method.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())


# IV. Accessing key-value pairs:
# We can print all the key-value pairs in the dictionary using items() method.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())  # NOTE :- WE GET TUPLE LIST

# USING LOOPS

# V. Accessing key-value by the loop with keys() function:
info = {'name':'Karan', 'age':19, 'eligible':True}
for key in info.keys():
    print(info[key])


# VI. Accessing key-value by the loop with values() function:
info = {'name':'Karan', 'age':19, 'eligible':True}
for value in info.values():
    print(value)


# VI. Accessing key-value by the loop with items() function:
info = {'name':'Karan', 'age':19, 'eligible':True}
for key,value in info.items():
    print(f" the key is {key} and the value is {value}")
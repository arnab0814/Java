'''Dictionary Methods'''

# update() :-
# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
# Example (1):
info = {'name':'Karan', 'age':19, 'eligible':True}
info1 = {'name2':'shubham', 'age1':19, 'eligible1':False}  # NOTE:-THE KEY NAME SHOULD BE DIFFERENT FROM THE PREVIOUS ,OTHERWISE IT WILL NOT UPDATE
info.update(info1)
print(info)
# Example (2):
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)


'''Removing items from dictionary:'''
# There are a few methods that we can use to remove items from dictionary.

# clear():
# The clear() method removes all the items from the list.\
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)


# pop():
# The pop() method removes the key-value pair whose key is passed as a parameter.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)


# popitem():
# The popitem() method removes the last key-value pair from the dictionary.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)


# values()	
# Returns a list of all the values in the dictionary
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
print(info.values())


# keys()
# Returns a list containing the dictionary's keys
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
print(info.keys())


# items()
# Returns a list containing a tuple for each key value pair
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
print(info.items())


# copy()	
# Returns a copy of the dictionary
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
co = info.copy()
print(co)


# get()
# Returns the value of the specified key
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
print(info.get('age'))


# setdefault()	
# Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# print(info.setdefault('name','karan'))   # Correct
# print(info.setdefault('name'))          
# Get the value of the "height" item, if the "height" item does not exist, insert "heigth" with the value "5'6":
print(info.setdefault('height',"5'6"))
print(info)


# fromkeys()
# Returns a dictionary with the specified keys and value
key = ('key1','key2','key3')
# value = 9,10,11
value = 9
item = dict.fromkeys(key,value)
print(item)

# Parameter	Description
# keys	Required. An iterable specifying the keys of the new dictionary
# value	Optional. The value for all keys. Default value is None




# del:
# we can also use the del keyword to remove a dictionary item.
# Example (1):
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)
# NOTE :- If key is not provided, then the del keyword will delete the dictionary entirely.
# Example (2):
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)






# update()
# clear()
# pop()
# popitem()
# values()
# keys()
# items()
# copy()
# get()
# setdefault()
# fromkeys()





# update()	Updates the dictionary with the specified key-value pairs
# clear()	Removes all the elements from the dictionary
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# values()	Returns a list of all the values in the dictionary
# keys() Returns a list containing the dictionary's keys
# items()	Returns a list containing a tuple for each key value pair
# copy()	Returns a copy of the dictionary
# get()	Returns the value of the specified key
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# fromkeys()	Returns a dictionary with the specified keys and value
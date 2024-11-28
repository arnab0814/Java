# LIST METHODS


# sort() :- 
# This method sorts the list in ascending order. The original list is updated
# Example 1:
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()                                   # NOTE :- WE CAN'T PRINT DIRECTLY SINCE IT DOESN'T RETURN RETURN THE LIST IT'S UPDATE THE LIST
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

# What if you want to print the list in descending order?
# We must give reverse=True as a parameter in the sort method.
# Example:
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)                       # NOTE :- WE CAN'T PRINT DIRECTLY SINCE IT DOESN'T RETURN RETURN THE LIST IT'S UPDATE THE LIST
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)

# The reverse parameter is set to False by default.
# NOTE :- Do not mistake the reverse parameter with the reverse method.


# reverse() :- 
# This method reverses the order of the list.
# Example:
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()                               # NOTE :- WE CAN'T PRINT DIRECTLY SINCE IT DOESN'T RETURN RETURN THE LIST IT'S UPDATE THE LIST
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)


# append() :-
# This method appends items to the end of the existing list.
# Example:
colors = ["voilet", "indigo", "blue"]
colors.append("green")                  # NOTE :- WE CAN'T PRINT DIRECTLY SINCE IT DOESN'T RETURN RETURN THE LIST IT'S UPDATE THE LIST
print(colors)


# insert() :-
# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
# Example:                              # NOTE :- WE CAN'T PRINT DIRECTLY SINCE IT DOESN'T RETURN RETURN THE LIST IT'S UPDATE THE LIST
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]
colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]
print(colors)


# remove()	
# Removes the first occurence item with the specified value
colors = ["voilet", "indigo", "blue", "green"]
colors.remove("blue")                           # NOTE :- WE CAN'T PRINT DIRECTLY SINCE IT DOESN'T RETURN RETURN THE LIST IT'S UPDATE THE LIST
print(colors)


# extend() :-
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
# Example 1:
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)                          # NOTE :- WE CAN'T PRINT DIRECTLY SINCE IT DOESN'T RETURN RETURN THE LIST IT'S UPDATE THE LIST
print(colors)


# index() :-
# This method returns the index of the first occurrence of the list item.
# Example:
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))


# count() :-
# Returns the count of the number of items with the given value.
# Example:
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))


# clear() :-
# Removes all the elements from the list
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.clear())


# pop() :-
# Removes the element at the specified position
colors = ["voilet", "indigo", "blue", "green"]
print(colors.pop(2))
print(colors)


# copy() :-
# Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
# Example:
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)


# Concatenating two lists:
# You can simply concatenate two lists to join two lists.
# Example:
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)







# append()
# clear()
# copy()
# count()
# extend()
# index()
# insert()
# pop()
# remove()
# reverse()
# sort()


# Google 


# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
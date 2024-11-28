# Tuple methods

# As tuple is immutable type of collection of elements it have limited built in methods.They are explained below

# count() :-
# The count() method of Tuple returns the number of times the given element appears in the tuple.
# Example:
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

# index() :-
# The Index() method returns the first occurrence of the given element from the tuple.
# Syntax:
# tuple.index(element, start, end)
# Example:
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
res = Tuple.index(3,6,8)
print('First occurrence of 3 is', res)
# NOTE :- This method raises a ValueError if the element is not found in the tuple.




# Manipulating Tuples
# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

# Example:
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)
# Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.

# However, we can directly concatenate two tuples without converting them to list.
# Example:
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)



# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
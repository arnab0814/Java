# Introduction to Loops
# Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

# for loop
# while loop


# The for Loop
# for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

# Example: iterating over a string:
name = 'Abhishek'
for i in name:
    print(i, end=", ")

# range():
# What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

# Here, we can use the range() function.

# Example:
for k in range(5):
    print(k)
    
    
    
    
# NOTE:- THROW BACK WHEN DON'T WANT A VALUE OF "i"

for _ in range(5):
    print("hellu")
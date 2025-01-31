'''Enumerate function in python'''
# NOTE :- Enumaretd fucntion makes the tuple with the value (index,element) and return a tuple and can be access by same as how we aceess a tuple ,also we can set how the numbering should be start of teh index



# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# NOTE :- As you can see, the enumerate function returns a tuple containing the index and value of each element in the sequence. You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above.



'''Changing the start index'''
# By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function:

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


# The enumerate function is often used when you need to loop over a sequence and perform some action with both the index and value of each element. For example, you might use it to loop over a list of strings and print the index and value of each string in a formatted way:

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')

# In addition to lists, you can use the enumerate function with any other sequence type in Python, such as tuples and strings. Here's an example with a tuple:

# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)

# And here's an example with a string:

# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)



marks = [12, 56, 32, 98, 12,  45, 1, 4]

index = 0
for mark in marks:
  print(mark)
  if(index == 3):
    print("Harry, awesome!")
  index +=1

for index, mark in enumerate(marks):
  print(mark)
  if(index == 3):
    print("Harry, awesome!")

for both in enumerate(marks, start=1):
  print(both)
# String Slicing & Operations on String

# Length of a String
    # We can find the length of a string using len() function.
    # Example:
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

# String as an array ,is like an array but not purely an array
# A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.
    # Example:
pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index


# NOTE :- This method of specifying the start and end index to specify a part of a string is called slicing.
# Slicing Example:
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index


# MY EXAMPLE 
str1 = "Slicing\string"

print(str1[ len(str1)-6 : len(str1)-2] ) # NOTE :- FOR MINUS SLICING THE STARTER NEGATIVE NUMBER SHOULD BE GRATER THAN THE STOPER NEGATIVE NUMBER

print(str1[-6:-2])
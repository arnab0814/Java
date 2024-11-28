# NOTE :- STRINGS ARE IMMUTABLE
# String methods
# Python provides a set of built-in methods that we can use to alter and modify the strings.


# upper() :
# The upper() method converts a string to upper case.
# Example:
str1 = "AbcDEfghIJ"
print("upper() :- ",str1.upper())

# isupper() :
# The isupper() method returns True if all the characters in the string are upper case, else it returns False.
# Example :
str1 = "WORLD HEALTH ORGANIZATION" 
print("isupper() :- ",str1.isupper())

# lower() :
# The lower() method converts a string to lower case.
# Example:
str1 = "AbcDEfghIJ"
print("lower() :- ",str1.lower())

# islower() :
# The islower() method returns True if all the characters in the string are lower case, else it returns False.
# Example :
str1 = "WORLD HEALTH ORGANIZATION" 
print("islower() :- ",str1.islower())

# casefold():
# Converts string into lower case
# Example
str1 = "THIS IS A STRING"
print("casefold() :- ",str1.casefold())

# swapcase():
# Swaps cases, lower case becomes upper case and vice versa
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
# Example
str1 = "converts THE STRING"
print("swapcase() :- ",str1.swapcase())

# capitalize() :
# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
# Example:
str1 = "hello"
print("capitalize() 1 :- ",str1.capitalize())
str1 = "hello WorlD"
print("capitalize() 2 :- ",str1.capitalize())


# strip() :
# The strip() method removes any white spaces before and after the string.
# Example:
str1 = "      Silver Spoon "
print("strip() :- ",str1.strip())


# rstrip() :
# the rstrip() removes any trailing characters. Starting trailling will not be removes
# Example:
str1 = "!!Hello !!!"
print("rstrip() :- ",str1.rstrip("!"))


# lstrip()	
# Returns a left trim version of the string
str1 = "!!!!!!!!! hello !"
print("lstrip() :- ",str1.lstrip())
    

# replace() :
# The replace() method replaces all occurences of a string with another string. Example:
# Example:
str1 = "Silver Spoon"
print("replace() :- ",str1.replace("Sp", "M"))


# split() :
# The split() method splits the given string at the specified instance and returns the separated strings as list items.
# Example:
str1 = "Silver Spoon"
print("split() :",str1.split(" "))      #Splits the string at the whitespace " ".


# rsplit()	
# Splits the string at the specified separator, and returns a list
str1 = "Silver spoon"
print("rsplit() :- ",str1.rsplit(" "))


# --> splitlines()	
# Splits the string at line breaks and returns a list
str1 = """This is
the line
paragraph
"""
print("Splitlines() :- ",str1.splitlines())


# center() :
# The center() method aligns the string to the center as per the parameters given by the user.
# Example:
str1 = "Welcome to the Console!!!"
print("center() 1 :- ",str1.center(50))

# We can also provide padding character. It will fill the rest of the fill characters provided by the user.
# Example:
str1 = "Welcome to the Console!!!"
print("center() 2 :- ",str1.center(50, "."))


# count() :
# The count() method returns the number of times the given value has occurred within the given string.
# Example:
str1 = "Abracadabra"
print("count() :- ",str1.count("a"))


# endswith() :
# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
# Example :
str1 = "Welcome to the Console !!!"
print("endswith() 1 :- ",str1.endswith("!!!"))

# We can even also check for a value in-between the string by providing start and end index positions.
# Example:
str1 = "Welcome to the Console !!!"
print("endswith() 2 :- ",str1.endswith("to", 4, 10))
#                            start,end :- index position                        


# startswith() :
# The endswith() method checks if the string starts with a given value. If yes then return True, else return False.
# Example :
str1 = "Python is a Interpreted Language" 
print("startswith() :- ",str1.startswith("Python"))


# find() :
# The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
# Example:
str1 = "He's name is Dan. He is an honest man."
print("find() 1 :- ",str1.find("is"))

# As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not. It returns -1
# Example:
str1 = "He's name is Dan. He is an honest man."
print("find() 2 :- ",str1.find("Daniel"))


# rfind()	
# Searches the string for a specified value and returns the last position of where it was found
str1 = "He's name is Dan. He is an honest man."
print("rfind() :- ",str1.rfind("is"))


# index() :
# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
# Example:
str1 = "He's name is Dan. Dan is an honest man."
print("index() 1 :- ",str1.index("Dan"))

# As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.
# print("index() 2 :-",str1.index("Daniel"))    # NOTE:- COMMENTED BECUSE IT SHOWS ERROR AS OUTPUT
# Example:
str1 = "He's name is Dan. Dan is an honest man."


# rindex()	
# Searches the string for a specified value and returns the last position of where it was found
str1 = "He's name is Dan. Dan is an honest man."
print("rindex() :- ",str1.rindex("is"))

# isnumeric()	
# Returns True if all characters in the string are numeric
str1 = "12345"
print("isnumeric :- ",str1.isnumeric())

# isalnum() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
# Example 1:
str1 = "WelcomeToTheConsole"
print("isalnum() :- ",str1.isalnum())


# isalpha() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
# Example :
str1 = "Welcome"
print("isalpha() :- ",str1.isalpha())


# sprintable() :
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
# Example :
str1 = "We wish you a Merry Christmas"  # NOTE:- SPECIAL CHAACTERS ARE NIT PRINTABLE like :- \n,\m,\r,etc.
print("sprintable() :- ",str1.isprintable())


# isspace() :
# The isspace() method returns True only and only if the string contains white spaces, else returns False.
# Example:
str1 = "        "       #using Spacebar
print("isspace() 1 :- ",str1.isspace())
str1 = "        "       #using Tab
print("isspace() 2 :- ",str1.isspace())


# istitle() :
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
# Example 1:
str1 = "World Health Organization" 
print("istitle() 1 :- ",str1.istitle())
# Example 2:
str1 = "To kill a Mocking bird"
print("istitle() 2 :- ",str1.istitle())

# title() :
# The title() method capitalizes each letter of the word within the string.
# Example:
str1 = "He's name is Dan. Dan is an honest man."
print("title() :- ",str1.title())


# rjust()	
# Returns a right justified version of the string 
str1 = "string"  # NOTE :- THE STRING SHOULD NIOT HAVE THE SPACE OR NEW LINE
print("rjust() :- ",str1.rjust(25))


# ljust()	
# Returns a left justified version of the string
str1 = "string"  # NOTE :- THE STRING SHOULD NIOT HAVE THE SPACE OR NEW LINE
print("ljust() :- ",str1.ljust(20))


# isdigit()	
# Returns True if all characters in the string are digits
str1 = "13434"
print("isdigit() :- ",str1.isdigit())


# isdecimal()	
# Returns True if all characters in the string are decimals (0-9)
str1 = "852"
print("isdecimal() :- ",str1.isdecimal())


# join()	
# Converts the elements of an iterable into a string
# Join all items in a tuple into a string, using a hash character as separator:
str1 = ["joining","the","list","into","string"]
print("join() :- ","".join(str1))   # NOTE :- USE GIVEN LIST OR TUPLE etc. AS ARGUMENT


# isascii()	
# Returns True if all characters in the string are ascii characters
str1 = "ijgpsfigi-493t8e=fg]q=eqor0j[k;cjgj[pe]]"
print("isascii() :- ",str1.isascii())


# expandtabs()	
# Sets the tab size of the string
str1 = "setting\tthe\ttab\tsize\tin\tthe\tstring"
print("expandtabs() :- ",str1.expandtabs(10))


# partition()	
# Returns a tuple where the string is parted into three parts
# Search for the word "bananas", and return a tuple with three elements:
# 1 - string before the "match"
# 2 - the "match"                                NOTE :- MATCH IS THE STRING YOU WANT TO SEARCH
# 3 - string after the "match"
str1 = "making a tuple with the match word differnce "
print("partition() :- ",str1.partition("match"))


# rpartition()	
# Returns a tuple where the string is parted into three parts
# Search for the last occurrence of the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
str1 = "making a tuple with the match word differnce with multiple match"
print("rpartition() :- ",str1.rpartition("match"))

# zfill()	
# Fills the string with a specified number of 0 values at the beginning
# Fill the string with zeros until it is long as a user wants:
str1 = "jsghos"
print("zfill() :- ",str1.zfill(34))


# isidentifier()	
# Returns True if the string is an identifier
# Idnetifier is a user defined name
str1 = "kjfsp"
print("isidentifier() :- ",str1.isidentifier())


# format()	
# Formats specified values in a string
# Insert the value inside the placeholder, the value should be in fixed point, in a decimal format:
str1 = "Your roll number is {rollno:.1f}"
print("format() :- ",str1.format(rollno= 115))


# format_map()	
# Formats specified values in a string
# NOTE :- THIS IS USE FOR DICTIONARY VALUES (MAXIMUM TIMES)
str1 = {"name":"Ramdas","rollno":"555"}
print("Your namae is {name} and roll no is {rollno}".format_map(str1))


# translate()	Returns a translated string
#Use a dictionary with ascii codes to replace, here 83 (S) with 80 (P): are ascii nos
# NOTE :- TANSLATOR TAKES dictionary AS ATTRIBUTE
# NOTE :- TRANLATOR WORKS WITH THE ascii NUMBERS , BUT WE CAN TRANSLATE AS PR OUR NEED WITH THE MAKE TRANSLATE FUNCTION
dict1 = {83:80}
str1 = "Sick"
print("translate() :- ",str1.translate(dict1))


# maketrans()	
# Returns a translation table to be used in translations
# Create a mapping table, and use it in the translate() method to replace any character:
str1 = "lick ilple"
maketranslator = str1.maketrans("li","pa")
print("maketrans() :- ",str1.translate(maketranslator))


# encode()	
# Returns an encoded version of the string
# NOTE :- ALWAYS USE ENCODED TEXT OR ALPHABET FOR THIS
str1 = "¶iya ho bihar ke lala"
print("encode() :- ",str1.encode('utf-8'))

print("¶".encode('utf-8'))

string = "123-¶" # utf-8 character

# ignore if there are any errors
print(string.encode('ascii', errors='ignore'))





# upper()
# isupper()
# lower()
# islower()
# casefold()
# swapcase()
# capitalize()
# strip()
# rstrip()
# center()
# count()
# endswith()
# find()
# rfind()
# index()
# rindex()
# isalnum()
# isnumeric()
# isalpha()
# isprintable()
# isspace()
# istitle()
# lstrip()
# replace()
# rsplit()
# split()
# splitlines()
# startswith()
# title()
# rjust()
# ljust()
# isdigit()
# isdecimal()
# join()
# isascii()
# expandtabs()
# partition()
# rpartition()
# zfill()
# isidentifier()
# format()
# format_map()
#  translate()
# maketrans()
# encode()


# VISIT WEBSITE google bhaiya jindabad


# --> upper()	Converts a string into upper case
# --> isupper()	Returns True if all characters in the string are upper case
# --> lower()	Converts a string into lower case
# --> islower()	Returns True if all characters in the string are lower case
# --> casefold()	Converts string into lower case
# --> swapcase()	Swaps cases, lower case becomes upper case and vice versa
# --> capitalize()	Converts the first character to upper case
# --> strip()	Returns a trimmed version of the string
# --> rstrip()	Returns a right trim version of the string
# --> center()	Returns a centered string
# --> count()	Returns the number of times a specified value occurs in a string
# --> endswith()	Returns true if the string ends with the specified value
# --> find()	Searches the string for a specified value and returns the position of where it was found
# --> rfind()	Searches the string for a specified value and returns the last position of where it was found
# --> index()	Searches the string for a specified value and returns the position of where it was found
# --> rindex()	Searches the string for a specified value and returns the last position of where it was found
# --> isalnum()	Returns True if all characters in the string are alphanumeric
# --> isnumeric()	Returns True if all characters in the string are numeric
# --> isalpha()	Returns True if all characters in the string are in the alphabet
# --> isprintable()	Returns True if all characters in the string are printable
# --> isspace()	Returns True if all characters in the string are whitespaces
# --> istitle()	Returns True if the string follows the rules of a title
# --> lstrip()	Returns a left trim version of the string
# --> replace()	Returns a string where a specified value is replaced with a specified value
# --> rsplit()	Splits the string at the specified separator, and returns a list
# --> split()	Splits the string at the specified separator, and returns a list
# --> splitlines()	Splits the string at line breaks and returns a list
# --> startswith()	Returns true if the string starts with the specified value
# --> title()	Converts the first character of each word to upper case
# --> rjust()	Returns a right justified version of the string
# --> ljust()	Returns a left justified version of the string
# --> isdigit()	Returns True if all characters in the string are digits
# --> isdecimal()	Returns True if all characters in the string are decimals (0-9)
# --> join()	Converts the elements of an iterable into a string
# --> isascii()	Returns True if all characters in the string are ascii characters
# --> expandtabs()	Sets the tab size of the string
# --> partition()	Returns a tuple where the string is parted into three parts
# --> rpartition()	Returns a tuple where the string is parted into three parts
# --> zfill()	Fills the string with a specified number of 0 values at the beginning
# --> isidentifier()	Returns True if the string is an identifier
# --> format()	Formats specified values in a string
# --> format_map()	Formats specified values in a string
# -->translate()	Returns a translated string
# --> maketrans()	Returns a translation table to be used in translations
# --> encode()	Returns an encoded version of the string
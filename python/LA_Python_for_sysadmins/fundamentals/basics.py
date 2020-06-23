#!/usr/bin/env python3.7

# Variables are assigned using the '=' assignment operator as follows:
my_str = "This is a simple string"

# We can print the value of the variable to the screen with:
print(my_str)

# Strings also work with assignment operators
stringConcat = 'pass' + 'word'
ha = 'Ha' * 4

"""
This is a
Triple Quoted String
"""

'''
This too
like OH EM GEE
'''

# You can add to the string:
my_str += " testing" # Would now output 'This is a simple string testing'

# We can then re-assign a value to the variable:
my_str = 1 # Would now output int 1.

# A function bound to an object is called a “method”. Here are some example methods that we can call on strings:

# Find() locates the first instance of a character (or string) in a string:
findS = "double".find('s') # This will return -1 Because it doesn't exist and can't give the location of it in the array representation of the characters
findU = "double".find('u') # This will return 2 Because 'u' is at array location 2 of the string
findBl = "double".find('bl') # This will return 3 Because 'bl' starts at array location 3 of the string

# .lower() method converts the string to lower case
"TeStInG".lower() # Will return 'testing'

# .upper() method converts the string to upper case
"TeStInG".upper() # Will return 'TESTING'

# Some escaped things as well:
print("Tab\tDelimited") # Will output -> Tab     Delimited
print("New\nLine") # Will output:
'''
New
Line
'''
print("Slash\\Character") # Will output -> Slash\Character
print("'Single' in Double") # Will output -> 'Single' in Double
print('"Double" in Single') # Will output -> "Double" in Single
print("\"Double\" in Double") # Will output -> "Double" in Double

# There are two main types of numbers that we’ll use in Python, int and float. These are int's:
2 + 2 # Addition
10 - 4 # Subtraction
3 * 9 # Multiplication
5 / 3 # Division
5 // 3 # Floor division, always returns a number without a remainder
8 % 3 # Modulo division, returns the remainder
2 ** 3 # Exponent (the power of)

# Converting data types
str(1.1) # Converts float to str '1.1'
int("10") # Converts str to int '10'
int(5.99999) #Converts float to int '5'
float("5.6") # Converts str to float '5.6'
float(5) # Converts int to float '5.0'

# Booleans are written as:
True
False

# Null or None is written as
None


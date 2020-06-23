####################
### Dictionaries ###
####################

# We create dictionary literals by using curly braces ({ and }), separating keys from values using colons (:), and separating key/value pairs using commas (,):
ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }

# We can read a value from a dictionary by subscripting using the key:
ages['kevin'] # Outputs the value associated with 'kevin' -> 59

# Keys can be added or changed using subscripting and assignment
ages['kayla'] = 21 # Full Dict is now -> {'kevin': 59, 'alex': 29, 'bob': 40, 'kayla': 21}

# Items can be removed from a dictionary using the del statement or by using the pop method:
del ages['kevin']
# AND:
ages.pop('alex')

# To find out what Keys or values we have, you can use the values() and keys() methods:
ages.keys() # Would return -> dict_keys(['bob', 'kayla'])
list(ages.keys()) # Would return -> ['bob', 'kayla']
ages.values() # Would return -> dict_values([59, 40])
list(ages.values()) # Would return -> [59, 40]

# You can also create dictionary items using the dict() function (2 ways):
weights = dict(kevin=160, bob=240, kayla=135)
colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])

#############
### Lists ###
#############

# A list is created in Python by using the square brackets [ and ] and separating the values by commas:
my_list = [1, 2, 3, 4, 5]

# To access the list value, call it's index as follows:
my_list[2] # Would return '3' from the list, i.e. the third value

# Additionally, we can access subsections of a list by “slicing” it. We provide the starting index and the ending index (the object at that index won’t be included):
my_list[0:2] # Returns -> [1, 2]
my_list[1:0] # Returns -> [2, 3, 4, 5]
my_list[:3] # Returns -> [1, 2, 3]
my_list[0::1] # Returns -> [1, 2, 3, 4, 5]
my_list[0::2] # Returns -> [1, 3, 5]

# Unlike strings which can’t be modified (you can’t change a character in a string), you can change a value in a list using the subscript:
my_list[0] = "a" # Outputs now -> ['a', 2, 3, 4, 5]

# You can use the .append() method to add to the end of th list:
my_list.append(6)
my_list.append(7) # Now outputs -> ['a', 2, 3, 4, 5, 6, 7]

# You can also concatenate lists:
my_list += [8, 9, 10] # Now outputs -> ['a', 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Replacing 2 sized slice with length 3 list, inserts new element
my_list[3:5] = ['d', 'e', 'f'] # Now outputs -> ['a', 2, 3, 'd', 'e', 'f', 6, 7, 8, 9, 10]

# We can remove a section of a list by assigning an empty list to the slice:
my_list[4:] = [] # Now Outputs -> ['a', '2', '3', 'd']

# Removing items from a list based on value can be done using the .remove method:
my_list.remove('d') # Now outputs -> ['a', '2', '3']

# Items can also be removed from the end of a list using the pop() method:
my_list.pop() # Now outputs -> ['a', '2']

# We can also use the pop method to remove items at a specific index:
my_list.pop(0) # Now outputs -> ['2']

# len() function returns the number of items in an object
len(my_list) # Would return '1'

##############
### Tuples ###
##############

# Tuples are a fixed width, immutable sequence type. We create tuples using parenthesis ( and ) and at least one comma (,):
point = (2.0, 3.0)

# We can use tuples in some operations like concatenation, but we can’t change the original tuple that we created (notice the comma at the end):
point_3d = point + (4.0,)

# One interesting characterist of tuples is that we can unpack them into multiple variables at the same time:
x, y, z = point_3d # where x, y, z is assigned 2.0, 3.0, 4.0 respectively

# The time you’re most likely to see tuples will be when looking at a format string that’s compatible with Python 2:
print("My name is: %s %s" % ("Keith", "Thompson")) # This substitutes %s with the tuple values after % placeholder


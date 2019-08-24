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


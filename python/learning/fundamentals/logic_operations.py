########################
### Logic Operations ###
########################

# The 'not' operation allows you to find if statement is false

name = ""
if not name:
    print("No Name Given")

# The 'or' operation evaluates true whether one OR the other argument is True

first = ""
last = "Thompson"
if first or last:
    print("The user has a first or last name")

# The 'or' operation will return the first value that is “truthy” or the last value in the chain

0 or 1  # Prints 1
1 or 2  # Prints 1

# The 'and' operation evaluates true when both arguments are True

first = "Keith"
last = ""
if first and last:
    print(f"Full name: {first} {last}")
elif first:
    print(f"First name: {first}")
elif last:
    print(f"Last name: {last}")

# The 'and' operation will return the first value that is “falsy” or the last value in the chain

0 and 1 # Prints 0
1 and 2 # Prints 2
(1 == 1) and print("Something") # Prints Something
(1 == 2) and print("Something") # Prints False


#########################
### input() function  ###
#########################

# Basically it just asks the user for input which you can use in the script. Example below:

name = input("What is your name? ")
birthdate = input("What is your birthdate? ")
age = int(input("How old are you? "))

print(f"\n{name} was born on {birthdate}")
print(f"Half of your age is {age / 2}")

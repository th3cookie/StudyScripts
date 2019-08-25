#################
### Functions ###
#################

# To start a function, type 'def' to define it

def hello_world():
    print("Hello, World!")

hello_world()

# Passing values to a function

def print_name(name):
    print(f"Name is {name}")

print_name("Larry")

# Returning values from a function

def add_two(num):
    return num + 2

result = add_two(4)
print(result)

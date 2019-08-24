################
### For Loop ###
################

for i in range(5):
    print(i)

# Continue rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop (i.e. the loop continues)
# Break terminates the current loop and resumes execution at the next statement (i.e. the loop breaks)

# Another 'for loop' example that will only print 'green' because 'continue' returns it back to the loop, then break, breaks the loop
colours = ['blue', 'green', 'red', 'purple']
for colour in colours:
    if colour == 'blue':
        continue
    elif colour == 'red':
        break
    print(colour)

# Another 'for loop' example, except this one iterates dict items and tuples with a key-value pair. calling the items() method pulls both sets of data as the item, assigning them to name, age while looping.
ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
for name, age in ages.items():
    print(f"Person Named: {name}")
    print(f"Age of: {age}")

##################
### While Loop ###
##################

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


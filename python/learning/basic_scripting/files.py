##########################
### Working with files ###
##########################

# https://docs.python.org/3/library/functions.html#open
# https://docs.python.org/3/glossary.html#term-file-object
# https://docs.python.org/3/library/io.html#io-overview

# Opening and Reading a File

xmen_file = open('files.txt', 'r')

print(xmen_file)

# Would output: <_io.TextIOWrapper name='files.txt' mode='r' encoding='UTF-8'>

# Thing to note is that reading the file makes it an array with \n characters e.g.

xmen_file.read()

# 'Storm\nWolverine\nCyclops\nBishop\nNightcrawler\n' is what it would read as

xmen_file.seek(0)

# When reading a file, think of it like a cursor position, it would take you to the end and stay there unless you seek back to where you want it to move and read from again. It works like array indexing per letter

# Another way that we can read through content is by using a for loop:

for line in xmen_file:
    print(line, end="")

# The print() function inserts a new line at the end, by default. Specify end="" because we don't want it to print \n characters when they're already in the file. 

xmen_file.seek(0)
for line in xmen_file:
    print(line)

# Remember you should close the file handle

xmen_file.close()

# To write to a file, use 'w' when opening it

xmen_file = open('files.txt')
new_xmen = open('new_xmen.txt', 'w')

new_xmen.write(xmen_file.read())
new_xmen.close()
new_xmen = open(new_xmen.name, 'r+')
new_xmen.read()

"""
Let's break that down:

1. We read from the base file and used the return value as the argument to write for our new file
2. We closed the new file.
3. We reopened the new file, using the r+ mode which will allow us to read and write content to the file.
4. We read the content from the new file to ensure that it wrote properly.
"""

# Now that we have a file that we can read and write from let’s add some more names:

new_xmen.seek(0)
new_xmen.write("Beast\n")
new_xmen.write("Phoenix\n")
new_xmen.seek(0)
new_xmen.read()

# Remember, seek works on index based on per character so this will overwrite the exact amount of characters as it needs, leaving the rest

# A fairly common thing to want to do is to append to a file without reading its current contents. This can be done with the 'a' mode. Two ways to do this:

with open('files.txt', 'a') as f:
    f.write('Professor Xavier\n')

f = open('files.txt', 'a')
with f:
    f.write("Something\n")

# An easy way to remember to close the file is to open it with the loop "with". This will automatically close it when the loop ends.

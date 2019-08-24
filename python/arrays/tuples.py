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


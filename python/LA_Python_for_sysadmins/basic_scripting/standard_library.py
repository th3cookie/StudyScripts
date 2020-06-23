#######################################
### Using Standard Library Packages ###
#######################################

# The python standard library -> https://docs.python.org/3/library/index.html

# To import it into your script, type 'import' and the library name

import time # https://docs.python.org/3/library/time.html

print(f"This is time.localtime() -> {time.localtime()}")  # https://docs.python.org/3/library/time.html#time.localtime

# Importing only certain modules from the time package makes them easier to call.

from time import localtime, mktime, strftime

print(f"This is localtime().tm_hour -> {localtime().tm_hour}")


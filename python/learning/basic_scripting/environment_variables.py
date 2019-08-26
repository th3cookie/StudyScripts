###################################
### Using Environment Variables ###
###################################

# The "os" package allows us to use 'env' variables

import os # https://docs.python.org/3/library/os.html

# Specifically these two modules from 'os':

from os import environ

"""
https://docs.python.org/3/library/os.html#os.environ

Example usage to see if we're working on a staging server with 'stage' set
In bash, you need to set:
STAGE=staging or STAGE=production
For this to work. But you can use anything from 'env' in bash.
"""

stage = os.environ["STAGE"].upper()

output = f"We're running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)

"""
https://docs.python.org/3/library/os.html#os.getenv

Another (easier) way to do the above is to use getenv
The above way will give you a KeyError if STAGE isn't set
Using getenv will allow you to set defaults in case a key isn't set
"""

from os import getenv

stage = os.getenv("STAGE", default="dev").upper()

# You can also do other things using 'os':

from os import chdir, getcwd, fchmod, fchown


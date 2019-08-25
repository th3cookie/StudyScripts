##################################
### Shell Commands from Python ###
##################################

# Using the Subprocess Module -> https://docs.python.org/3/library/subprocess.html

import subprocess
proc = subprocess.run(
    ['ls', '-l'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

# proc would return -> CompletedProcess(args=['ls', '-l'], returncode=0, stdout=<The Successful Command>, stderr='b')

# To print the output of the command without byte literals
print(proc.stdout.decode())

# check=True allows for stderr printing
new_proc = subprocess.run(['cat', 'fake.txt'], check=True)


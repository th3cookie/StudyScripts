#################################
### sys argument and argparse ###
#################################

import sys  # https://docs.python.org/3/library/sys.html

print(f"First argument {sys.argv[0]}")  # argv[0] will always be the script itself

print(f"Positional arguments: {sys.argv[1:]}")

import argparse # https://docs.python.org/3/library/argparse.html

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()
print(args)


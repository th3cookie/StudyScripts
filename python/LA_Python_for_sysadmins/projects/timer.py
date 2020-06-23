#!/usr/bin/env python3.6

# time library -> https://docs.python.org/3/library/time.html

from time import localtime, mktime, strftime

start_time = localtime()
print(f"Timer started at {strftime('%X', start_time)}")

# Wait for user to stop timer
input("Press any key to stop timer ")

stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print(f"Timer stopped at {strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")

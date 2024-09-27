#!/usr/bin/env python3

# Author: Biniyam sundedo
# Author ID: 123236218
# Date Created: 2024/09/25

import sys

# Check if a command-line argument is provided
if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Assign the value of the first argument to 'timer'
else:
    timer = 3  # Assign the default value of 3 if no argument is provided

# WHILE loop that repeats until (and not including when) timer equals 0
while timer > 0:
    print(timer)
    timer -= 1

# Print final message after the loop ends
print("blast off!")

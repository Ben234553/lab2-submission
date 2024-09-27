#!/usr/bin/env python3

# Author: Biniyam sundedo
# Author ID: 123236218
# Date Created: 2024/09/25

import sys

# Assigning the value of int(sys.argv[1]) to the object 'timer'
timer = int(sys.argv[1])

# While loop that repeats until timer equals 0
while timer > 0:
    print(timer)
    timer -= 1

# Print final message after the loop ends
print("blast off!")

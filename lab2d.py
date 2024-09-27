#!/usr/bin/env python3

import sys

# Check if exactly 2 arguments are provided
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(0)  # Exit with code 0 to indicate a successful termination

# Assign the first argument to the object 'name' and the second to 'age'
name = sys.argv[1]
age = sys.argv[2]

# Print the exact output
print(f"Hi {name}, you are {age} years old.")






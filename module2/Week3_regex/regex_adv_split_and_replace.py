#!/usr/bin/env python3


import re

print('Hello')

## split , using regex as seperator

## notice you don't need to \ escape characters inside []
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))

# to include the split delimiter characters too, use a capturing group
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))


## Using sub to substitute
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[ REDACTED ]", "Received an email for go_nuts95@my.example.com"))


## Rearrange name example
# \1 - 1st capturing group
# \2 - 2nd capturing group
#  Read up on 'backreferences'
print(re.sub(r"^([\w .-]*), ([\w .-]*)$" , r"\2 \1", "Lovelace, Ada" ))
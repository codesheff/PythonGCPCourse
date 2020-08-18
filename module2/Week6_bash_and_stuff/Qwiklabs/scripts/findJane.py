#!/usr/bin/env python3

#import os
#files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3 )

## Not done this yet

file='../data/list.txt'
with open(file,'r') as f:
    for line in file:
        print(line)


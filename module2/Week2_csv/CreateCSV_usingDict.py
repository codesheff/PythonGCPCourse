#!/usr/bin/env python3

import csv
import os

datadir='data'

outputfile=os.path.join(datadir,"by_department.csv")


if ( not(os.path.exists(datadir))):
    print('Creating output dir')
    os.mkdir(datadir)
else:
    pass


# Store users as list of dictionaries
users = [ 
     {"name": "Rod", "username": "rod001", "department": "IT infrastructure"}
    ,{"name": "Jane", "username": "jan001", "department": "IT Music"}
    ,{"name": "Freddy", "username": "fred001", "department": "IT Dancing"}
]

keys = [ "name", "username", "department"]


with open(outputfile,'w') as by_department:
    writer = csv.DictWriter(by_department,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

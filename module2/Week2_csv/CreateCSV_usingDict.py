#!/usr/bin/env python3

import csv
import os, sys

this_script_path=(os.path.dirname(sys.argv[0]))
this_script_name=(os.path.basename(sys.argv[0]))
datadir=os.path.join(this_script_path,"../data")

outputfile=os.path.abspath(os.path.join(datadir,"by_department.csv"))


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

print('Written ' + outputfile)
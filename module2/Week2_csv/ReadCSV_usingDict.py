#!/usr/bin/env python3

import csv
import os

datadir='data'

outputfile=os.path.join(datadir,"by_department.csv")

print("path is " + datadir)
if ( not(os.path.exists(datadir))):
    print('Creating output dir')
    os.mkdir(datadir)
else:
    print('Output dir exist')
    
#keys = [ "name", "username", "department"]
with open(outputfile,'r') as by_department:
    reader = csv.DictReader(by_department)
    for row in reader:
        print(("User {} has username {} and works in department {}.").format(row["name"], row["username"], row["department"]))

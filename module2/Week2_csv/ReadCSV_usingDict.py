#!/usr/bin/env python3

import csv
import os, sys

this_script_path=(os.path.dirname(sys.argv[0]))
this_script_name=(os.path.basename(sys.argv[0]))
datadir=os.path.join(this_script_path,"../data")

outputfile=os.path.abspath(os.path.join(datadir,"by_department.csv"))


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

print('Read ' + outputfile)
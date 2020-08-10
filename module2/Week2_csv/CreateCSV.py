#!/usr/bin/env python3

import csv
import os, sys


this_script_path=(os.path.dirname(sys.argv[0]))
this_script_name=(os.path.basename(sys.argv[0]))
datadir=os.path.join(this_script_path,"../data")

outputfile=os.path.abspath(os.path.join(datadir,"hosts.csv"))

if ( not(os.path.exists(datadir))):
    print('Creating output dir')
    os.mkdir(datadir)
else:
    pass

hosts = [ ["hostA","192.168.1.1"],["host2","192.168.1.2"],["host3","192.168.1.3"]]

with open(outputfile,'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

print('Written ' + outputfile)
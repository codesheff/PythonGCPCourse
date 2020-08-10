#!/usr/bin/env python3

import csv
import os, sys

datadir='data'

this_script_path=(os.path.dirname(sys.argv[0]))
this_script_name=(os.path.basename(sys.argv[0]))
datadir=os.path.join(this_script_path,"../data")

outputfile=os.path.abspath(os.path.join(datadir,"hosts.csv"))


#outputfile=os.path.join(datadir,"hosts.csv")

#hosts = [ ["hostA","192.168.1.1"],["host2","192.168.1.2"],["host3","192.168.1.3"]]

with open(outputfile,'r') as hosts_csv:
    reader = csv.reader(hosts_csv)
    
    for row in reader:
        # row is a list . Unpack the list into the variables
        hostname, ip_address = row
        print("Hostname: {} , IP-Address: {}".format(hostname, ip_address))

print('Read ' + outputfile)
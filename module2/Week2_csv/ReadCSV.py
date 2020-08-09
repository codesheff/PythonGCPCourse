#!/usr/bin/env python3

import csv
import os

datadir='data'

outputfile=os.path.join(datadir,"hosts.csv")

#hosts = [ ["hostA","192.168.1.1"],["host2","192.168.1.2"],["host3","192.168.1.3"]]

with open(outputfile,'r') as hosts_csv:
    reader = csv.reader(hosts_csv)
    
    for row in reader:
        # row is a list . Unpack the list into the variables
        hostname, ip_address = row
        print("Hostname: {} , IP-Address: {}".format(hostname, ip_address))

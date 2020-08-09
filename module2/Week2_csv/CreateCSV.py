#!/usr/bin/env python3

import csv
import os

datadir='data'

outputfile=os.path.join(datadir,"hosts.csv")

hosts = [ ["hostA","192.168.1.1"],["host2","192.168.1.2"],["host3","192.168.1.3"]]

with open(outputfile,'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

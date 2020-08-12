#!/usr/bin/env python3


print('Hello')

import sys
import argparse

import re

parser = argparse.ArgumentParser()

parser.add_argument("--logfile", type=str, dest="logfile", help="the logfile to be processed", default="/etc/hosts")

args = parser.parse_args()


print('logfile is :' + args.logfile )

#logfile = sys.argv[1]
logfile = args.logfile 
interesting_thing='ip'
with open(logfile,'r') as f:
    for line in f:
        if interesting_thing not in line:
            continue
        # Do some pattern matchign , to get some info
        # and then print it out
        print(line.strip())



# We're using the syslog, and we want to display the date, time, and process id 
# that's inside the square brackets. 
# We can read each line of the syslog and pass the contents to the show_time_of_pid 
# function. 
# Fill in the gaps to extract the date, time, and process id from the passed line, 
# and return this format: Jul 6 14:01:23 pid:29440.

def show_time_of_pid(line):
    #               date                time                      pid
    pattern = r"^\b(\w{3} \d{1,2})\b \b(\d{1,2}:\d{2}:\d{2})\b.*\[(\d{1,})\]"
    result = re.search(pattern, line)
    return "{} {} pid:{}".format(result[1],result[2],result[3])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187
print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440
print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807
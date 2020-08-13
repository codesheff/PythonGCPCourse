#!/usr/bin/env python3


print('Hello')

import sys
import argparse

import re
import os 

this_script_path=(os.path.dirname(sys.argv[0]))
print('this_script_path:' + this_script_path)

this_script_name=(os.path.basename(sys.argv[0]))
datadir=os.path.join(this_script_path,"data") # Ah!  you don't want the '/' in your args - makes sense!

print('datadir:' + datadir)
default_logfile=os.path.join(datadir,"syslog_example")
print('default is :' + default_logfile)

# Set up input options
parser = argparse.ArgumentParser()
parser.add_argument("--logfile", type=str, dest="logfile", help="the logfile to be processed", default=default_logfile)
args = parser.parse_args()


print('logfile is :' + args.logfile )

#logfile = sys.argv[1]
logfile = args.logfile 
interesting_thing='CRON'
usernames={} # create empty dictionary 
with open(logfile,'r') as f:
    for line in f:
        if interesting_thing not in line:
            continue
        # Do some pattern matching , to get some info
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)

        if result is None:
            continue
        
        name = result[1]
        usernames[name] = usernames.get(name,0) + 1  #tell get to  use default of '0'

print(usernames)


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

#print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
#print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
#print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187
#print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440
#print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807



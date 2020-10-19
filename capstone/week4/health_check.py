#!/usr/bin/env python3

#!/usr/bin/env python3

import os
import shutil
import sys
import socket
import psutil




def check_disk_full():
    """Returns True if there isn't enough disk space. False otherwise."""
    du = shutil.disk_usage("/")
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    #gigabytes_free = du.free / 2**30
    if percent_free < 20:
        return True
    return False

def check_cpu_constrained():
    """ Returns True if the cpu is having too much usage, False otherwise."""
    return psutil.cpu_percent(1) > 80

def check_localhost_not_resolving():
    """Returns True if it fails to resolve 127.0.0.1 to 'localhosts."""

 
    try:
        return socket.gethostbyaddr('127.0.0.1')[0] != 'localhost'
    except:
        return True

def check_memory_constrained():
    """ Returns True if the memory is having too much usage, False otherwise."""
    available = psutil.virtual_memory().available
    available_in_MB = available / 1024 ** 2 #convert to MB
    return available_in_MB < 500
    
def send_email(subject):  #generate email information
  import emails

  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  #subject in params
  body = "Please check your system and resolve the issue as soon as possible."
  attachment = ""
  
  #generate email for the online fruit store report and pdf attachment
  message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(message)

def main():
    
    # Define list of checks, and error messages.
    checks=[
        (check_localhost_not_resolving,"Error - localhost cannot be resolved to 127.0.0.1"),
        (check_cpu_constrained,"Error - CPU usage is over 80%"),
        (check_memory_constrained, "Error - Available memory is less than 500MB"),
        (check_disk_full, "Error - Available disk space is less than 20%")
    ]

    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            send_email(msg)
            everything_ok = False

    if not everything_ok:
        sys.exit(1)
        
    print('Everything ok.')
    sys.exit(0)


main()
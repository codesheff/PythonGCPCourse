#!/usr/bin/env python3
import sys
import os
import re
import argparse


def error_search(log_file):
    #error = input("What is the error? ")
    error = 'stetest' #hardcoding so I can debug

    returned_errors = []
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in  file.readlines():
            #Create list of error patterns, as the word 'error' , plus whatever words user inputs.
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
                # If all the patterns are matched, the include that in the list of returned errors
                if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                    returned_errors.append(log)
        file.close()
    return returned_errors

  
def file_output(returned_errors):
    #with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    outfile=os.path.join(datadir,"errors_found.log")
    with open(outfile, 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()

if __name__ == "__main__":
    this_script_path=(os.path.dirname(sys.argv[0]))
    print('this_script_path:' + this_script_path)
    
    this_script_name=(os.path.basename(sys.argv[0]))
    datadir=os.path.join(this_script_path,"../data") # Ah!  you don't want the '/' in your args - makes sense!
    
    print('datadir:' + datadir)
    default_logfile=os.path.join(datadir,"fishy.log")
    print('default is :' + default_logfile)
    
    # Set up input options
    parser = argparse.ArgumentParser()
    parser.add_argument("--logfile", type=str, dest="logfile", help="the logfile to be processed", default=default_logfile)
    args = parser.parse_args()
    
    print('logfile is :' + args.logfile )
    #logfile = sys.argv[1]
    log_file = args.logfile 
    #log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)
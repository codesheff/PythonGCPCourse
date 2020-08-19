#!/usr/bin/env python3



import argparse, os, sys



def search_logfile(log_file):
    
    import re

    #Initialise your dictionary
    error_messages = {}
    per_user = {}
    
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log_entry in  file.readlines():
            #print(log_entry)

            pattern = r'ticky: INFO ([\w ]*) '
            result = re.search(pattern, log_entry)         
            if result:
                print(log_entry)
                message_type='INFO'
                user = result[1]
            
            pattern = r'ticky: ERROR ([\w ]*) '
            result = re.search(pattern, log_entry)         
            if result:
                print(log_entry)
                message_type='ERROR'
                user = result[1]

            print(log_entry)
            print(user)
            print(message_type)

            #Create list of error patterns, as the word 'error' , plus whatever words user inputs.
            #error_patterns = ["error"]
            #for i in range(len(error.split(' '))):
            #    error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            #    # If all the patterns are matched, the include that in the list of returned errors
            #    if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
            #        returned_errors.append(log)
        file.close()
    return error_messages, per_user


if __name__ == "__main__":
    this_script_path=(os.path.dirname(sys.argv[0]))
    print('this_script_path:' + this_script_path)
    
    this_script_name=(os.path.basename(sys.argv[0]))
    datadir=os.path.join(this_script_path,"") # Ah!  you don't want the '/' in your args - makes sense!
    
    print('datadir:' + datadir)
    default_logfile=os.path.join(datadir,"syslog.log")
    print('default is :' + default_logfile)
    
    # Set up input options
    parser = argparse.ArgumentParser()
    parser.add_argument("--logfile", type=str, dest="logfile", help="the logfile to be processed", default=default_logfile)
    args = parser.parse_args()
    
    print('logfile is :' + args.logfile )
    #logfile = sys.argv[1]
    log_file = args.logfile 

   


    ## Read log file
    search_logfile(log_file)
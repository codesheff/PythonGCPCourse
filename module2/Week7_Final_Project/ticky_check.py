#!/usr/bin/env python3



import argparse, os, sys



def search_logfile(log_file):
    
    import re

    #Initialise your dictionary
    error_messages = {}  # 
    per_user = {}        # username, INFO count , ERROR count
    
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log_entry in  file.readlines():
            #print(log_entry)

            message_type=''

            pattern = r"ticky: INFO ([\w ]*) *(\[.*\])? *\((\w*)\)$"
            result = re.search(pattern, log_entry)         
            if result:
                message_type='INFO'
                user = result[3]
            

            pattern = r"ticky: ERROR ([\w ]*) *(\[.*\])? *\((\w*)\)$"
            result = re.search(pattern, log_entry)         
            if result:
                message_type='ERROR'
                user = result[3]
                error_type = result[1]
                error_messages[error_type] = error_messages.get(error_type,0) + 1

            
            # Add one to the dictionary entry
            if message_type :
                per_user[(user,message_type)] = per_user.get((user,message_type),0) + 1
                

    return error_messages, per_user


def WriteOuput(error_messages, per_user):

    import csv
    import operator

    outputfile=os.path.abspath(os.path.join(datadir,"error_counts.csv"))
    
    if ( not(os.path.exists(datadir))):
        print('Creating output dir')
        os.mkdir(datadir)
    else:
        pass
    
        
    keys= [ "ERROR", "count"]
       ## sort the dictionaries, and put them into list of dictionaries ( to be written to csv)
    #import operator
    #sorted( error_messages.items(), key=operator.itemgetter(0))
    

  



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
    error_messages = {}
    per_user = {}
    error_messages, per_user = search_logfile(log_file)

    print(per_user)





    ## write the output files
   # WriteOuput(error_messages, per_user)
    
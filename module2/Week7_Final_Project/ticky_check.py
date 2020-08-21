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

            #pattern = r"ticky: INFO ([\w ]*) *(\[.*\])? *\((.*)\)$"
            pattern = r"ticky: INFO ([\w ']*)(\[.*\])?.*\((.*)\)$"
            result = re.search(pattern, log_entry)         
            if result:
                message_type='INFO'
                user = result[3]
            

            #pattern = r"ticky: ERROR ([\w ]*) *(\[.*\])? *\((.*)\)$"
            pattern = r"ticky: ERROR ([\w ']*)(\[.*\])?.*\((.*)\)$"
            
            result = re.search(pattern, log_entry)         
            if result:
                message_type='ERROR'
                user = result[3]
                error_type = result[1]
                error_messages[error_type] = error_messages.get(error_type,0) + 1

            
            # Add one to the dictionary entry
            ## Should be in format { 'bob' : { user : bob, info: 1 , error: 2} }
        #mydict = { 
        #   'mdouglas':  { 'user' : 'mdouglas', 'INFO': 2 , 'ERROR' : 1 }
        #   ,'fred':     { 'user' : 'fred'    , 'INFO': 3 , 'ERROR' : 3 }
        # }

            if message_type:  # Add record if it's matched a pattern
                mytemp_dict=per_user.get(user,{ 'user' : user })
                mytemp_dict[message_type] = mytemp_dict.get(message_type,0) + 1
                per_user[user] = mytemp_dict
            else:
                print('Not recognising:' + log_entry)

            
                
        return error_messages, per_user


def WriteOutput(error_messages, per_user):

    import csv
    import operator

    outputfile=os.path.abspath(os.path.join(datadir,"error_counts.csv"))
    
    if ( not(os.path.exists(datadir))):
        print('Creating output dir')
        os.mkdir(datadir)
    else:
        pass
    
        
    ## Write error count file
    outputfile=os.path.abspath(os.path.join(datadir,"error_message.csv"))
    with open(outputfile,'w') as f:
        writer = csv.writer(f)#
        writer.writerow(['Error', 'Count'])
        writer.writerows(sorted( error_messages.items(), key = operator.itemgetter(1), reverse = True))

    ## Write User count file

    
    #Create list of dictionaries
    per_user_list=[]
    for item in per_user.items():
        per_user_list.append(item[1])

    keys = [ "user", "INFO", "ERROR"]

    outputfile=os.path.abspath(os.path.join(datadir,"user_statistics.csv"))
    with open(outputfile,'w') as f:
        writer = csv.DictWriter(f,fieldnames=keys)
        writer.writeheader()
        writer.writerows(sorted(per_user_list, key = operator.itemgetter('user')))

        

    
    

  



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

    
    ## write the output files
    WriteOutput(error_messages, per_user)
    
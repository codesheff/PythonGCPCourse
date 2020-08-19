#!/usr/bin/env python3



import argparse, os, sys






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
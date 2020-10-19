#!/usr/bin/env python3


def process_file(file):
    
    import requests
   
    print('Processing ' + file)
    url = "http://localhost/upload/"
    with open(file, 'rb') as opened:
        r = requests.post(url, files={'file': opened})


        
    
    

def main():
    print('Hello again!')
    
    import os

    for filename in os.listdir(datadir):
        if filename.endswith('.jpeg'):
            file=os.path.join(datadir,filename)
            process_file(file)
        





if __name__=='__main__':
    import os
    import sys

    this_script_path=(os.path.dirname(sys.argv[0]))
    this_script_name=(os.path.basename(sys.argv[0]))
    datadir=os.path.abspath(os.path.join(this_script_path,"supplier-data","images/"))
    outdir=datadir

    main()
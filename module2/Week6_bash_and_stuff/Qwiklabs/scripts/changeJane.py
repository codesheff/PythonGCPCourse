#!/usr/bin/env python3

import sys
import subprocess


file=sys.argv[1]

print(file)

with open(file,'r') as f:
    for oldname in f.readlines():
        oldname = oldname.strip()
        newname=oldname.replace('jane','jdoe').strip()
        #print(newname)
        command = ['mv ', oldname, newname ]
        #print(command)
        #result = ( subprocess.run( command ))
        # This runs the command,  and captures just the return code
        result = (subprocess.run([ 'mv', oldname, newname ]))
        #print(result.stderr) 
    
    f.close()




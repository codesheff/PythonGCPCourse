#!/usr/bin/env python3

import subprocess
import sys
print(sys.version)

# This runs the command,  and captures just the return code
result = (subprocess.run('date'))

print('Result is:')
print('return code is:' + str(result.returncode))


## Use capture_output=True  to capture stdout and stderr
result = (subprocess.run('date',capture_output=True))

print('Result is:')
print('stdout, as array of bytes:' + str(result.stdout)) # a this point , its an array of bytes

# decode the array of bytes, using default of UTF-8

print('stdout -decoded as  UTF-8 ' + str(result.stdout.decode().split())) 

#  and split it
print(result.stdout.decode().split())


## list a file that doesn't exist

def run_command(command):

    print('Running command "' + command + '"')
    command_as_list=command.split()
    result = subprocess.run(command_as_list,capture_output=True)
    print('stderr:')
    print(result.stderr)
    print('stdout:')
    print(result.stdout)
    print('returncode :')
    print(result.returncode)


run_command('ls -l /tmp_not_exist')
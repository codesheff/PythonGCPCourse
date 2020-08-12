#!/usr/bin/env python3

import os

print('Hello')

## os.eviron.get  - allows you to specify default if its not found
print('HOME:' + os.environ.get('HOME',''))
print('PATH:' + os.environ.get('PATH',''))
print('SHELL:' + os.environ.get('SHELL',''))
#print('FRUIT:' + os.environ['FRUIT']) - this would error, as it does not exist
print('FRUIT:' + os.environ.get('FRUIT','')) # this will return the '' default you specify

os.environ['FRUIT'] = 'Pineapple'
print('FRUIT:' + os.environ.get('FRUIT',''))


#!/usr/bin/env python3

#Import libraries
import csv
import re

import os, sys

import PIL
import PIL.Image

this_script_path=(os.path.dirname(sys.argv[0]))
this_script_name=(os.path.basename(sys.argv[0]))
datadir=os.path.join(this_script_path,"../images")
outdir='/opt/icons'


def process_file(root,filename):
    
    #from PIL import Image
    file=os.path.join(root,filename)
    print('Processing ' + file)
    
    
    image=PIL.Image.open(file)

   
    #size =  (128, 128)
    #image.resize(size)
    #image.thumbnail(size)
    #image.rotate(-90)

    
    #outfile = os.path.join(outdir,filename)
    outfile = os.path.join(outdir,'stetest.jpg')
    image.save(outfile, "JPEG")
    #return new_name


def main():
    for root, dirs, files in os.walk(datadir):
        for filename in files:
            if filename == '.DS_Store':
                continue
            
            #print(root + ' ' + filename )
            process_file(root,filename)
            break

main()

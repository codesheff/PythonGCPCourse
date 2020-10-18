#!/usr/bin/env python3

#Import libraries

import os, sys

this_script_path=(os.path.dirname(sys.argv[0]))
this_script_name=(os.path.basename(sys.argv[0]))
datadir=os.path.abspath(os.path.join(this_script_path,"../images"))
#outdir='/opt/icons'
outdir='/f/stedo/mygit/PythonGCPCourse/capstone/week1/icons'


def process_file(file):
    
    import os
    import PIL
    from PIL import Image
    #file=os.path.join(root,filename)
    print('Processing ' + file)
    
    
    image=PIL.Image.open(file)

    #size =  (128, 128)
    #image.resize(size)
    #image.rotate(-90)
    #image.convert('RGB')

    outfile = os.path.join(outdir,os.path.basename(file)).split('.')[0] 
   
    image.rotate(-90).convert('RGB').resize((128,128)).save(outfile,'jpeg')
    
   
           
    print('saving as ' + outfile)
    
  
    image.close()

def main():
    import os

    for filename in os.listdir(datadir):
        if filename.startswith('.'):       # skip files that start with '.'
            continue
            
        #print(root + ' ' + filename )
        file=os.path.join(datadir,filename)
        process_file(file)
        

main()

#!/usr/bin/env python3

from PIL import Image

import os, sys

#user=os.getenv('USER')
#images_dir='/home/{}/images/'.format(user)

this_script_path=(os.path.dirname(sys.argv[0]))
this_script_name=(os.path.basename(sys.argv[0]))
datadir=os.path.abspath(os.path.join(this_script_path,"../images"))
#outdir='/opt/icons'
outdir='/f/stedo/mygit/PythonGCPCourse/capstone/week1/icons'

for image_name in os.listdir(datadir):
    if not image_name.startswith('.'):
        image_path= os.path.join(datadir, image_name)
        im=Image.open(image_path)
        new_path=os.path.join(outdir, image_name.split('.')[0])
        im.rotate(-90).convert('RGB').resize((128,128)).save(new_path,'jpeg')
        im.close()
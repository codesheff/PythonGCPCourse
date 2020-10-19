#!/usr/bin/env python3

print('hello')

#Note: The raw images from images subdirectory contains alpha transparency layers. 
# So, it is better to first convert RGBA 4-channel format to RGB 3-channel format before processing the images.
#  Use convert("RGB") method for converting RGBA to RGB image.



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
    outfile =outfile + '.jpeg'
   
    image.convert('RGB').resize((600,400)).save(outfile,'jpeg')
    
   
           
    print('saving as ' + outfile)
    
  
    image.close()




def main():
    print('Hello again!')
    
    import os

    for filename in os.listdir(datadir):
        if filename.endswith('.tiff'):
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
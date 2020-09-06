#!/usr/bin/env python3

from concurrent import futures
import argparse
import logging
import os
import sys

import PIL
import PIL.Image

from tqdm import tqdm


def process_options():

    kwargs = {
        'format': '{%(levelname)s] %(message)s',
    }

    parser = argparse.ArgumentParser(
        description='Thumbnail generator',
        fromfile_prefix_chars='@'
    )

    parser.add_argument('--debug', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-q', '--quiet', action='store_true')

def process_file(root,basename):
    filename=f'{root}/{basename}'
    image=PIL.Image.open(filename)

    size =  (128, 128)
    image.thumbnail(size)

    new_name = f'thumbnails/{basename}'
    image.save(new_name, "JPEG")
    return new_name
    

## Not sure if anything more above this

def progress_bar(files):
    return tqdm(files, desc='Processing', total=len(files) ,dynamic_ncols=True)


def main_threaded():

    process_options()

    # Create the thumbnails directory
    if not os.path.exists('thumbnails'):
        os.mkdir('thumbnails')

    executor = futures.ThreadPoolExecutor()

    for root, _, files in os.walk('images'):
        for basename in progress_bar(files):
            if not basename.endswith('.jpg'):
                continue
            executor.submit(process_file, root, basename)
        
    return 0 

def main_processpool():

    process_options()

    # Create the thumbnails directory
    if not os.path.exists('thumbnails'):
        os.mkdir('thumbnails')

    executor = futures.ProcessPoolExecutor()

    for root, _, files in os.walk('images'):
        for basename in progress_bar(files):
            if not basename.endswith('.jpg'):
                continue
            executor.submit(process_file, root, basename)
        
    return 0 
        
def main_orig():

    process_options()

    # Create the thumbnails directory
    if not os.path.exists('thumbnails'):
        os.mkdir('thumbnails')

    for root, _, files in os.walk('images'):
        for basename in progress_bar(files):
            if not basename.endswith('.jpg'):
                continue
            process_file(root, basename)
        
    return 0 

if __name__ == "__main__":
    sys.exit(main_processpool())
#!/usr/bin/env python

## No idea what I'm doing here

import subprocess
from multiprocessing import Pool
import os
import sys



def run(dirname):
  print("Input: {} {} {}".format(src, dest, dirname))
  subprocess.call(["rsync", "-arq", os.path.join(src,dirname), os.path.join(dest,dirname)])


if __name__ == "__main__":

  this_script_path=(os.path.dirname(sys.argv[0]))
  print('this_script_path:' + this_script_path)

  
  src = os.path.join(this_script_path,"../data/prod")
  dest = os.path.join(this_script_path,"../data/prod_backup2")

  for (root, dirs, files) in os.walk(src):
    print(dirs)
    break # for 1-depth

  p = Pool(len(dirs)) # Create Pool of tasks, one for each dir
  p.map(run, dirs)  # map each thing in Pool to a run of 'run' function
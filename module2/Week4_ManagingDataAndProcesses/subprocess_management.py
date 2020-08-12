#!/usr/bin/env python3

import os 
import subprocess

import re

# Make a copy of my env
my_env = os.environ.copy()

# Alter that copy
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

# Run a subprocess with that env 
result = subprocess.run(['env'], env=my_env, capture_output=True)

result2=(re.search(r"PATH", result.stdout.decode()))
print(result2[0])
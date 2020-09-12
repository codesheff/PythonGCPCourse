#!/usr/bin/env python3

import psutil

print(psutil.cpu_percent())


print(psutil.disk_io_counters())
print(psutil.net_io_counters())


# run a os command
import subprocess

src = './scripts'
dest = './scripts_syncd_to'

subprocess.call(["rsync", "-arq", src, dest])


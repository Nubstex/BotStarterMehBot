#!/usr/bin/python
import os
import subprocess
print("start")
os.system("chmod +rwx -v ./start.sh")
subprocess.call(['sh', './start.sh'])
os.system("chmod +rwx -v ./Nubot-code/run.py")
os.chdir('Nubot-code')
import run
print("end")

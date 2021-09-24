#!/usr/bin/python
import os
import subprocess

print("start")

os.system("chmod +rwx -v *")
subprocess.call(['sh', './start.sh'])

os.system("chmod +rwx -v ./nubot-code2/run.py")
os.chdir('nubot-code2')

key = 'TOKEN'
value = os.getenv('TOKEN')
print("Value of 'TOKEN' environment variable :", value) 

os.system('pip install ffmpeg-python')
os.system("chmod +rwx -v *")
os.system('python run.py')
print("end")

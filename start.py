#!/usr/bin/python
import os
import subprocess

print("start")

os.system("chmod +rwx -v *")
subprocess.call(['sh', './start.sh'])

os.system("chmod +rwx -v ./MehBot/run.py")
os.chdir('MehBot')

key = 'TOKEN'
value = os.getenv('TOKEN')
print("Value of 'TOKEN' environment variable :", value) 

os.system('pip install ffmpeg-python')
os.system("chmod +rwx -v *")
os.system('python run.py')
print("end")

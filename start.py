#!/usr/bin/python
import os
import subprocess

print("start")

os.system("chmod +rwx -v ./start.sh")
subprocess.call(['sh', './start.sh'])

os.system("chmod +rwx -v ./Nubot-code/run.py")
os.chdir('Nubot-code')

key = 'TOKEN'
value = os.getenv('TOKEN')
print("Value of 'TOKEN' environment variable :", value) 

my_env = os.environ.copy()
my_env["PATH"] = "/usr/bin/env:" + my_env["PATH"]
subprocess.Popen('run.py', env=my_env)

print("end")

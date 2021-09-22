#! /usr/bin/env python
import os
import subprocess
print("start")
os.system("chmod +rwx -v ./start.sh")
subprocess.call("./start.sh")
print("end")

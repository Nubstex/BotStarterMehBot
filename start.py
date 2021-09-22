import os
import subprocess
print("start")
os.system("chmod +rwx -v ./start.sh")
subprocess.call(['sh', './start.sh'])
print("end")

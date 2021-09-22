import os
import subprocess
print("start")
os.system("chmod +rwx -v ./start.sh")
subprocess.run("./start.sh")
print("end")

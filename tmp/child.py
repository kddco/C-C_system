import sys 
import subprocess
import time
import os
SaveDirectory = os.getcwd() #印出目前工作目錄
theproc = subprocess.Popen([sys.executable, SaveDirectory+ "\\reg.py"])
theproc.communicate()
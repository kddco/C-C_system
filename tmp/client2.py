import sys
import subprocess
import time
import os
import socket

TCP_IP = 'localhost'
TCP_PORT = 9177
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
with open('dir.exe', 'wb') as f:
    print ('file opened')
    while True:
        #print('receiving data...')
        data = s.recv(BUFFER_SIZE)
        print(data)
        if not data:
            f.close()
            break
        # write data to a file
        f.write(data)

print('Successfully get the file')
print('connection closed')
# os.system("pause")

excutionFile = "dir.exe"
SaveDirectory = os.getcwd() #印出目前工作目錄
theproc = subprocess.Popen([sys.executable,excutionFile])
theproc.communicate()
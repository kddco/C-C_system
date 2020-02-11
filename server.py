# server2.py
import socket
from threading import Thread


TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print(" New thread started for "+ip+":"+str(port))

    def run(self):
        filename='sample.txt'
        f = open(filename,'rb')

        self.sock.send(bytes("Translating ... ", "utf-8"))
        while True:
            l = f.read(BUFFER_SIZE)
            self.sock.send(l)
            if not l:
                f.close()
                self.sock.close()
                print(print("The thread closed "+ip+":"+str(port)))
                break

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print ("Waiting for incoming connections...")
    (conn, (ip,port)) = tcpsock.accept()
    print ('Got connection from ', (ip,port))
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)
    for t in threads:
        t.join()
    # print(threads)

# for t in threads:
#     t.join()
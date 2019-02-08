# echo_client.py
import socket
import sys

mot=[]

#inter host address
host = '192.168.207.140'    
port = 9999                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
#s.sendall(b'Hello, world')
try:
    d= int(s.recv(1024).decode())
    print("this is my d:",d)
    n= int(s.recv(1024).decode())
    print("this is my n:",n)
    while True:
        data = s.recv(64)
        if data:
            i=0
            data=int(data.decode())
            mot.append(data)
            sys.stdout.isatty()
            sys.stdout.write('.')
            sys.stdout.flush()
        else:
            print(" ")
            break
finally:
    for i in range(len(mot)):
        mot[i] = chr((mot[i]**d)%n)
        #print("progress:",int((i*100)/len(mot)),"%         \r"),
    print(''.join(mot))
    s.close()


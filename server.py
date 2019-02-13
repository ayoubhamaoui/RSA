# server.py 
import socket                                         
import time
import pickle
import random
import time

check = True

prime=[]
prime.append(2)
def prime_List():
  L=[]
  L.append(2)
  for i in range(3,100):
    check=True
    for  j in L:
        if not (i%j):
            check=False
    if check:
        L.append(i)
  return L

prime=prime_List()


def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1


#gcd function
def gcd(a,b):
  if(b==0):
    return a
  else:
    r=a%b
    return gcd(b,r)

#function to check if number is prime
def is_prime(x):
   if x >= 2:
      for y in range(2,x):
        if not ( x % y ):
          return False
   else:
     return False
   return True



p = q = 2
def find(p,q):
  i= random.randint(0, len(prime))
  j= random.randint(0, len(prime))
  p,q = prime[i],prime[j]
  return p,q

#find two prime number in prime list
p,q = find(p,q)



#calculate n=p*q
n=p*q

#calculate fn
fn = (p-1)*(q-1)

#select integer e / gcd(fn,e)=1, 1 < e < fn
while(True):
 e = random.randint(2,fn-1)
 if(gcd(fn,e) == 1):
   break


#calculate d / d*e = 1 mod(fn)
d=modInverse(e,fn)

#public key {e,n}
#private key {d,n}

#Encryption: M<n, C= M^e (mod n)
#Decryption C, M= C^d(mod n)

#inter text to encrypt
data = input("Enter Text: ")
dataE=[]
dataD=[]
for i in range(0,len(data)):
  C=(ord(data[i])**e)%n
  dataE.append(C)


#my string Decrepted
for i in dataE:
  m=(i**d)%n
  dataD.append(chr(m))




# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 


host = '192.168.207.140'                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))
    #send data
    #dataE = pickle.dumps(dataE)
    clientsocket.sendall(str(d).encode())
    print("Send d: ",d)
    time.sleep(1)
    clientsocket.sendall(str(n).encode())
    print("Send n: ",n)
    for car in dataE:
      clientsocket.sendall(str(car).encode())
      time.sleep(1)

    clientsocket.close()







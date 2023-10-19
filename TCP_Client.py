import socket
import random
from time import sleep
from datetime import datetime


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9999))
while True:
    number = random.randint(0, 100)
    sock.send(str(number).encode('utf-8'))
    sleep(2)
    #resp = sock.recv(1024)
    #print(resp.decode('utf-8'))

sock.close()
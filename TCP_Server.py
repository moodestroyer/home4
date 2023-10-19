import socket
from time import sleep
from datetime import datetime
import csv


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost', 9999))
sock.listen(5) # максимум подключений
while True:
    client, addr = sock.accept() # ожидание подключения, блокировка
    print('Connected: ', addr)
    while True:
        data = client.recv(1024) # чтение, блокировка
        now = datetime.now()
        udata = data.decode('utf-8')
        with open("lab2.csv", mode="a", encoding='utf-8') as file:
            file_writer = csv.writer(file, delimiter="\t")
            file_writer.writerow([now.strftime("%H:%M:%S"), udata])
        #client.send(udata.upper().encode('utf-8')) # запись, блокировка

    client.close()
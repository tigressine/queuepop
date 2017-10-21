#! /usr/bin/env python3
import socket
import time
import random

def main():
    TARGET = '54.227.77.179'
    PORT = 4711
    sendme = "queuepopped".encode()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TARGET, PORT))
    #time.sleep(random.randint(5,10)) 
    sock.send(sendme)
    
    while True:
        reply = sock.recv(10)
        print(reply)
        time.sleep(1)
        if reply:
            print(reply.decode())
            break
    
    sock.close()

if __name__ == '__main__':
    main()

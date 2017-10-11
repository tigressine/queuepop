#! /usr/bin/env python3
import socket

def main():
    TARGET = '54.227.77.179'
    PORT = 4711

    sendme = "trust me".encode()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TARGET, PORT))
    sock.send(sendme)
    sock.close()

if __name__ == '__main__':
    main()

import socket
import time
from collections import deque
from random import randrange

class EchoServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind((self.host, self.port))

    def echo_loop(self):
        print("Staring echo-server")
        while True:
            data, cl_addr = self.server.recvfrom(4096)
            print(f"New message from client {cl_addr}")
            self.server.sendto(data, cl_addr)

if __name__ == "__main__":
    ser = EchoServer("ponger", 8001)
    ser.echo_loop()


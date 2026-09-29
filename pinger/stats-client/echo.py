import socket
import time
from collections import deque
from threading import Timer

class EchoClient:
    """ Get RTT stats by sending timestamp in an echo packet
    that the server (running at host, port) echoes back """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.rtt = deque([])
        self.num_entries = 0
        self.limit = 10
        self.mean = 0
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def calculate_rtt(self):
        mean = 0
        for i in self.rtt:
            mean = mean + i
        if len(self.rtt):
            mean = mean/len(self.rtt)
        print(f"Mean RTT = {mean}")

    def send_ping(self):
        epoch_time = int(time.time())
        time_str = str(epoch_time)
        self.client.sendto(time_str.encode(), (self.host, self.port))
        data, addr = self.client.recvfrom(4096)
        time_str = data.decode()
        rtt = int(time.time()) - int(time_str)
        # Pop entries from the front when new data is received, LIFO
        if (len(self.rtt) > 10):
            item = self.rtt.popleft()
        self.rtt.append(rtt)
        self.calculate_rtt()
        # Keep monitoring the path periodically
        self.start()

    def start(self):
        """ Start gathering RTT metrics """
        self.timer = Timer(5, self.send_ping)
        self.timer.start()

if __name__ == "__main__":
    cl = EchoClient("localhost", 8001)
    cl.start()

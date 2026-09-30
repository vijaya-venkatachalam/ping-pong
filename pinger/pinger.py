#!/usr/bin/python3
from stats.echo import EchoClient

mon = EchoClient("proxy", 8080)
print(f"Starting client for proxy at {mon.host}:{mon.port}")
mon.start()

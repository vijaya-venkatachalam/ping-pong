#!/usr/bin/python3
from stats-client.echo import EchoClient

mon = EchoClient("ponger", 8001)
mon.start()

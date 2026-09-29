#!/usr/bin/python3
from stats.echo import EchoClient

mon = EchoClient("ponger", 8001)
mon.start()

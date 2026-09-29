from stats-server.server import EchoServer

ser = EchoServer("ponger", 8001)
ser.echo_loop()


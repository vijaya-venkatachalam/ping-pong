from backend.balancer import Balancer

myproxy = Balancer("proxy", 8080, "ponger", 8001)
myproxy.proxy_server()


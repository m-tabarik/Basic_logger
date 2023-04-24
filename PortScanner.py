import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
        target  = socket.gethostbyname(sys.argv[1])
else:
    print("Arguments not profound")


print("-"*50)
print("Scanning target: "+target)
print("Start Time: "+str(datetime.now()))
print("-"*50)


try:
        for port in range(79,85):
                s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result =s.connect_ex((target,port))
                if result == 0:
                   print(f"port {port} is open")
                s.close( )
except KeyboardInterrupt:
      print("\n Exiting-----------------")
      sys.exit()
except socket.gaierror:
        print("Hostname could'nt resolved-------------------")
        sys.exit()
except socket.error:
      print("Known Error------------------")
      sys.exit()

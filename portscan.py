#!/bin/python

import sys
import pyfiglet 
import socket
from datetime import datetime
ascii_banner = pyfiglet.figlet_format("PORT SCANNER") 
print(ascii_banner) 
            #scanning the target
if len(sys.argv) == 2:
	target=socket.gethostbyname(sys.argv[1])
else:
	print("Hostname is missing ")
#banner	
print("-"*50)
print("Started Scanning at"+" "+target)
print("started timing"+" "+str(datetime.now())) 
print("-"*50) 
print("\n")

try:
	for port in range(50,85):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #target and port
		socket.setdefaulttimeout(1)
		#print("Connecting {}".format(port))
		res=s.connect_ex((target,port)) #returns an err
		if res == 0:
		   print("The port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\n exiting connection")
	sys.exit()	
			
except socket.gaierror:
       print("\n hostname is not correct")
       sys.exit()
       
except socket.error:
	print("\n Connection refused")   
	sys.exit() 
	   	
		
	

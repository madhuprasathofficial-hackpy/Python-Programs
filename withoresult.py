import socket
import os
 
s = socket.socket()
 
s.settimeout(5)
 
status = s.connect_ex(("127.0.0.1", 443))
 
if status == 0:
	print("[+] Port 443 is OPEN")
else:
    print(f"[-] Port 443 is CLOSED")
    print(f"Error Code : {status}")
    print(f"Reason 	: {os.strerror(status)}")


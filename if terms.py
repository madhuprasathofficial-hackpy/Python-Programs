import socket
s=socket.socket()
s.settimeout(5)
status=s.connect_ex(("127.0.0.1",443))
if status==0:
    print("[+]port 443 is OPEN")
else:
    print("[-]port 443 is CLOSED")
    print(f"Errorcode:{ststus}")
if status==10061:
    print("Reason:operation would block")
elif status==10035:
    print("reason:operation would block")
else:
    print("Reason:unknown")

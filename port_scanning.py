from socket import socket,AF_INET,SOCK_STREAM

Ip = input("Enter the ip address:")
startingport = int(input("Enter starting port number:"))
endingport = int(input("Enter ending port number:"))
print(f"Scanning ports {startingport} to {endingport} on {Ip}")
for i in range(startingport, endingport+1):
    sock = socket(AF_INET,SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((Ip, i))
    if result == 0:
        print(f"Port {i} is open")
    else:
        print(f"Port {i} is closed")
    sock.close()

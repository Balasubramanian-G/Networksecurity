import subprocess

Ip = input("Enter the ip address:")
command = ["nmap",Ip]
print(f"Running basic Nmap scan on {Ip}..")
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)

Networksecurity-Portscanning
This project tells the implementation of networksecurity concept(Portscanning) using python programming language.

Description:
Task-1
      The first task is about scanning the network to identify which ports are open and close.Firt it uses python's pacakage-socket to create a virtual endpoint and it gets a ip address (Ipv4)and port range (starting port number and ending port number) and simply scans and tells which one is open/close.It doesn't use any automation tool.

Task-2
      The second task is same as the first task.It performs the scanning operation to identify which port is open/close.The main difference is the automation tool Network mapper(N-map) used in the task-2.It uses the pythons subprocess module for the operation.The N-map tool not only print which ports open or close it can also include additional informations like services which are running on the port and their version .

Library used:
Task-1 socket
Task-2 subprocess
Sample output:Task-1
![Screenshot 2025-06-11 181923](https://github.com/user-attachments/assets/4d4b16e8-6796-4903-a32e-584617a630ba)
Task-2
![Screenshot 2025-06-11 183011](https://github.com/user-attachments/assets/6b6b5a2a-e883-4e2c-b6f2-57be7540188d)



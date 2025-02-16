# Team-7
| Name        | Github Username           |
| ------------- |:-------------:|
| Daniel Rodriguez      | drod7946 |
| Jayden Hamilton      | jswizzle325      |
| Austen Lee | buzzerstrafe      |
| Yannick Tchio Tiombo | yttiombo      |

Instructions:

For server.py and client.py : UDP Socket Configuration
First run the server; it will prompt you to enter your IP address choice (which clients will use to connect), then enter it and the server will listen for incoming client messages. After running the server, run the client; it will prompt you to enter the same server IP address. Then the equipment ID to the server via UDP socket.
The server receives the ID, broadcasts it to all connected clients, and sends an acknowledgment back to the client that send the ID. Each client listens for incoming broadast from the server and receives new equipment IDs added by clients. 

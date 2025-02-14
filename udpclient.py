import socket

# Allow configuration for network selection
serverIP = input("Enter the server IP address (default 127.0.0.1): ") or "127.0.0.1"
serverPort = 7501
bufferSize = 1024

# Create a UDP socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    # User inputs equipment ID to transmit
    equipment_id = input("Enter Equipment ID to send (or 'exit' to quit): ").strip()
    if equipment_id.lower() == "exit":
        print("Exiting client...")
        break
    
    # Send equipment ID to the server
    UDPClientSocket.sendto(equipment_id.encode(), (serverIP, serverPort))

    # Receive server response
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    print(f"Server Response: {msgFromServer[0].decode()}")

# Close the socket when exiting
UDPClientSocket.close()

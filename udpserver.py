import socket

# Allow configurable network selection
localIP = input("Enter the IP address to bind to (default 127.0.0.1): ") or "127.0.0.1"
receivePort = 7501
broadcastPort = 7500
bufferSize = 1024

# Create the UDP socket for receiving 
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, receivePort))  # Bind to the selected network interface

# Create the UDP socket for broadcasting
broadcastSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
broadcastSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print(f"UDP Server up and listening on {localIP}:{receivePort}")

while True:
    # Receive data from clients (players)
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0].decode('utf-8')
    address = bytesAddressPair[1]
    print(f"Received: {message} from {address}")

    # Extract equipment ID from the message 
    equipment_id = message.strip()

    # Broadcast the equipment ID to all clients on the network
    broadcastMessage = f"Equipment {equipment_id} added!"
    broadcastSocket.sendto(broadcastMessage.encode(), ("<broadcast>", broadcastPort))
    print(f"Broadcasted: {broadcastMessage}") 

    # Reply to the sender
    UDPServerSocket.sendto("Equipment received".encode(), address)



































##import socket


#Allow configuarable network selection
##localIP = input("Enter the IP address to bind to (default 127.0.0.1): ") or "127.0.0.1" 
##receivePort = 7501
##broadcastPort = 7500
##bufferSize = 1024


# Create the UDP socket for receiving 
##UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # UDP socket creation
##UDPServerSocket.bind((localIP, receivePort))  # Bind to all available network interfaces

# Create the UDP socket for broadcasting
##broadcastSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
##broadcastSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
##print(f"UDP Server up and listening on {localIP}:{receivePort}")

##while True:
    # Receive data from clients (players)
    ##bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    ##message = bytesAddressPair[0].decode('utf-8')
    ##address = bytesAddressPair[1]
    ##print(f"Received: {message} from {address}")

    # Extract equipment ID from the message 
    ##equipment_id = message.strip()

    # Broadcast the equipment ID to all clients on the network
    ##broadcastMessage = f"Equipment {equipment_id} added!"
    ##broadcastSocket.sendto(broadcastMessage.encode(), ("<broadcast>", broadcastPort))
    ##print(f"Broadcasted: {broadcastMessage}") 

    # Reply to the sender
    ##UDPServerSocket.sendto("Equipment received".encode(), address)
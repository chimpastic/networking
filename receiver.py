import socket

# Define the server address and port  # Replace with the IP address of the server you want to communicate with
server_port = 12345  # Replace with the port number you want to use

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port for receiving messages
udp_socket.bind(('0.0.0.0', server_port))

# Function to send a message
#def send_message():
#    message = input("Enter a message to send: ")
#    udp_socket.sendto(message.encode(), (server_ip, server_port))

# Function to receive and print a message
def receive_message():
    data, addr = udp_socket.recvfrom(1024)
    print(f"Received message from {addr}: {data.decode()}")

# Main loop for sending and receiving messages
while True:
    receive_message()

# Close the socket when done
udp_socket.close()


import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address):
    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            print(f"Connection with {client_address} closed.")
            break
        print(f"Received message from {client_address}: {message}")
        
        # Echo the message back to the client
        client_socket.send(f"Server received: {message}".encode('utf-8'))

# Configure server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))  # Change 'localhost' to your server's IP address if needed
server.listen(5)

print("Server started. Waiting for connections...")

while True:
    client_socket, client_address = server.accept()
    print(f"Connection from {client_address} established.")
    
    # Create a thread for each client
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()

import socket
import threading

# Configure client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8888))  # Change 'localhost' to the server's IP address

# Function to send messages
def send_message():
    while True:
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            break

# Function to receive messages
def receive_message():
    while True:
        response = client.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")

# Start sending and receiving messages in separate threads
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()

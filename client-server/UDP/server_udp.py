import socket

def main():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a public host, and a port
    server_socket.bind(('0.0.0.0', 9999))

    print("Server is ready to receive messages")

    while True:
        # Receive data from the client
        data, address = server_socket.recvfrom(1024)
        print(f"Received {data.decode('utf-8')} from {address}")

        # Send a response back to the client
        server_socket.sendto(b'ACK', address)

if __name__ == '__main__':
    main()
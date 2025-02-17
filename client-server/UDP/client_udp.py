import socket

def main():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define the server address and port
    server_address = ('localhost', 9999)

    # Send data to the server
    client_socket.sendto(b'Hello, Server', server_address)

    # Wait for a response from the server
    data, server = client_socket.recvfrom(4096)
    print(f"Received {data.decode('utf-8')} from {server}")

    # Close the socket
    client_socket.close()

if __name__ == '__main__':
    main()
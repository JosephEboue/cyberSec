import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    #create the socket object and specifies the address family, which in our case is IPv4
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #binding the socket 
    server.bind((IP, PORT))
    #sets up the server to listen for incoming connections, with a backlog of 5 (it can queue up to 5 connection requests before refusing new ones)
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        #continuously accepts new connections and blocks until a new connection is made 
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        #for each new connection, a new thread is created to handle client communication, ensuring that the server can handle multiple clients concurrently that's wh ywe call it multithreaded TCP server at the beginning
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        #data is received from the client with a buffer size of 1024 bytes (random you can change this)
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        #some response is sent back to the client 
        sock.send(b'200 - OK')


if __name__ == '__main__':
    main()
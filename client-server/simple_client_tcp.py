import socket

IP = '127.0.0.1'
PORT = 9998

#define a send_message function that takes a message argument
def send_message(message):
    #create a socket object client using socket.socket() and connect to the server using the client.connect() method, specifying the IP address and port of the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))
    #send test message encoding the message to bytes using utf-8 encoding
    client.send(message.encode('utf-8'))
    #receive a response from the server using the client.recv() method, specifying a buffer size of 4096 bytes (you can change this if you want)
    response = client.recv(4096)
    #print the received response, decoding it from bytes to a string using utf-8 encoding
    print(f'Received response from server : {response.decode("utf-8")}')
    #close the connection
    client.close()

if __name__ == '__main__':
    print(f'\n--- Enter messages to send to {IP}:{PORT} or write `quit` to exit ---\n')
    while True:
        message = input("Enter a message to send: ")
        send_message(message)
        if message=='quit':
            break
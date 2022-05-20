from http import client
import socket


HEADER = 64
PORT = 5050  # Which port should the server use, 5050 just because. Use something is not being used for something else.
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.15" # Address of server, for now its the local ip address of machine we are running the server in
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) # Socket connects requires a tuple of server address, port.


def send(msg):
    message = msg.encode(FORMAT) # Encode into byte format first.
    msg_length = len(msg)
    send_length = str(msg_length).encode('utf-8')
    send_length += b' ' * (HEADER - len(send_length)) # Pads message length to make sure it folows the HEADER/FORMAT of 64 in this case.
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Miguel")
input()
send(DISCONNECT_MESSAGE)
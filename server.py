import socket
import threading

HEADER = 64
PORT = 5050  # Which port should the server use, 5050 just because. Use something is not being used for something else.
SERVER = "192.168.1.15" # ipconfig on cmd, get ipv4 address, its your local ipv4 address. We are running the server on local network.
SERVER = socket.gethostbyname(socket.gethostname()) # This gets the ip above for you, its better to do it this way.  
ADDR = (SERVER, PORT) # Tuple of server ip and port.
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

#print(SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating a socket, type AF_INET, SOCK_STREAM just means its streaming data. Family, type.
server.bind(ADDR) # Bound address to socket, needs tuple

# Handles communication between client and server.
def handle_client(conn, addr): # Happens concurrently
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)  # Waits till it receives message from client, using header as the byte size. Deconde from byte format to string.
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT) # This is the actual message of length, msg_length.

        if msg == DISCONNECT_MESSAGE:
            connected = False

        print(f"[{addr}] {msg}")

    conn.close()

# Allow server to start listening to connections and make them.
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()  # This line waits for a new connection to the server.
        thread = threading.Thread(target = handle_client, args=(conn, addr)) # Make a new thread to handle communication between new connection and server.
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") # Show how many active connections there currently are.

print("[STARTING] Server is starting...")
start()
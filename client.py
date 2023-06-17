import socket

# Get the IP address of the host
IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def main():
    # Create a client socket and connect to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

    connected = True
    while connected:
        # Prompt the user for input
        msg = input("> ")

        # Send the message to the server
        client.send(msg.encode(FORMAT))

        if msg == DISCONNECT_MSG:
            # If the user wants to disconnect, break the loop
            connected = False
        else:
            # Receive and print the server's response
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")

    # Close the client socket after disconnecting from the server
    client.close()

if __name__ == "__main__":
    main()

import socket
import threading
import wikipedia

import socket
import threading
import wikipedia

# Server configuration
IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # Receive message from the client
        msg = conn.recv(SIZE).decode(FORMAT)

        if msg == DISCONNECT_MSG:
            connected = False

        print(f"[{addr}] {msg}")

        # Process the message using Wikipedia summary
        try:
            summary = wikipedia.summary(msg, sentences=1)
        except wikipedia.exceptions.DisambiguationError as e:
            summary = str(e.options)
        except wikipedia.exceptions.PageError:
            summary = "No summary found for the given query."

        # Send the summary back to the client
        conn.send(summary.encode(FORMAT))

    conn.close()


def main():
    print("[STARTING] Server is starting...")

    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the server to the specified address and port
    server.bind(ADDR)

    # Listen for incoming connections
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        # Accept a new client connection
        conn, addr = server.accept()

        # Create a new thread to handle the client
        thread = threading.Thread(target=handle_client, args=(conn, addr))

        # Start the thread
        thread.start()

        # Print the number of active connections
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == "__main__":
    main()

from os import waitpid
# first of all import the socket library
import socket

ONE_CONNECTION_ONLY = (True)
# Create a socket object
sock = socket.socket()
print ("Socket successfully created") 

# Create a text file 
fileName = "file.txt"

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345
host = socket.gethostname()
# Bind to the port
sock.bind((host, port))
print("Socket binded to %s " %(port))

# put socket into listning mode
sock.listen(10)
print("Socket is listening")

while True:
    # Establish a connection with client
    conn, addr = sock.accept()
    print(f"Accepted connection from {addr}")
    data = conn.recv(12345)
    print(f"Server recieved data {data}")
    with open (fileName, "rb") as file:
    # read data from txt file
        data = file.read(12345)

    # keep reading the data
        while data:
            conn.send(data)
            print(f"Sent {data!r}")
            data = file.read(12345)
    print("file Sent completed :)")

# Close the connection
    conn.close()
# check if there is only one connection
    if(ONE_CONNECTION_ONLY):
        break
# shutdown the socket
sock.shutdown(1)

# Close the connection with client
sock.close()
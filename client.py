
# Import socket module
import socket

# Create a socket object
sock = socket.socket()

# Define the port on which you want to connect.
host = socket.gethostname()
port = 12345

# connect to the server 
sock.connect((host, port))

# sending a hello message from client to server
sock.send(b"Hello from client")
with open("recievedFile.txt","wb") as file:
    print("File opened")
    print("receiving data....")

    # keep recieving th edata from the server
    while True:
        data = sock.recv(12345)
        print(f"data = {data}")
        print(sock.recv(12345))
        if not data:
            break
        file.write(data)

print("Got the file")

# Close the connection
sock.close()
print("Connection is closed")


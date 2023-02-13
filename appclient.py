import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def ClientSend(youfile):
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)
    print(youfile)
    """ Opening and reading the file data. """
    file = open(youfile, "r")
    data = file.read()
    file_extension = youfile[youfile.rfind(".") + 1:]
    file_name = youfile[youfile.rfind("/") + 1:youfile.rfind(".")]
    combined_file_name = file_name + "." + file_extension
    print(combined_file_name)
    """ Sending the filename to the server. """
    client.send(f"results/{combined_file_name}".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Sending the file data to the server. """
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Closing the file. """
    file.close()

    """ Closing the connection from the server. """
    client.close()



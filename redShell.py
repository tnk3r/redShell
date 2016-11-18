import socket

## User Input for Red Camera

address = raw_input("Enter IP of RDC Camera:  ")
print "Connecting to :"+str(address)

## socket setup

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Connection

sock.connect((str(address), 1111))

## Read a little bit of data

print sock.recv(256)

while True:
    print "Command Structure:  "
    print " #$ EXT: S or G or H : command : value : newline"
    print "example: #$EXT:S:SENSFPS:48001:\\n"

    ## Ask user for Red Camera Command input

    command = raw_input("RCP Command:  ")

    ## If User enters Q the program will quit.

    if command == "Q":
        break

    ## Send Command

    sock.sendall(str(command))

    ## Read a little Data

    print sock.recv(256)

import socket, sys

# Command line input for IP Address
try:
    address = str(sys.argv[1])
except:
    address = raw_input("Enter IP of RDC Camera:  ")

print "Connecting to: "+str(address)

## socket setup

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Connection

sock.connect((str(address), 1111))

## Read a little bit of data

print sock.recv(256)

while True:
    print "\nexample: #$EXT:S:SENSFPS:48001:"
    print "\nQ/q to quit.\n"

    ## Ask user for Red Camera Command input

    command = raw_input("RedShell$:  ")

    ## If User enters Q the program will quit.

    if command == "Q" or command == 'q':
        break

    ## Send Command

    sock.sendall(str(command)+"\n")

    ## Read a little Data

    print sock.recv(256)

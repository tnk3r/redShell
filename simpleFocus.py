import socket, time
address = raw_input("Enter IP of RDC Camera:  ")
print "Connecting to :"+str(address)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((str(address), 1111))

while True:
    print "Enter a number between (0-655) to set Focus Encoder Position."
    value = raw_input("Set Encoder Value:  ")
    if value != "Q" or value != 'q':
        sock.sendall("#$EXT:S:HCFOCUS:"+str(int(value)*100)+":\n")
    else:
        break

import socket, time
address = raw_input("Enter IP of RDC Camera:  ")
print "Connecting to :"+str(address)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((str(address), 1111))

def floop():
    for i in range(50, 66):
        if i != "":
            sock.sendall("#$EXT:S:HCFOCUS:"+str(int(i)*1000)+":\n")
            time.sleep(0.25)

while True:
    print "Enter a number between (0-655) to set Focus Encoder Position."
    value = raw_input("Set Encoder Value:  ")
    if value == "loop":
        floop()
    if value != "Q":
        sock.sendall("#$EXT:S:HCFOCUS:"+str(int(value)*100)+":\n")
    else:
        break

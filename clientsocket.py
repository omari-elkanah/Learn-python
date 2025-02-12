import socket
print('######################################################\n');print("Do NOT forget to change PORT AND SERVER IP IN CLIENT");print('\n######################################################\n\n')
#server= '169.254.17.216' #nic ip
server2='192.168.23.117' #ip by connection
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr=socket.gethostbyname(socket.gethostname())
Cname=socket.gethostname()
print(f"Your hostname is {Cname}")
print("waiting..");print("waiting...")
print("waiting....")
PORT= 5090; header=64; format="utf-8"
Addr=(server2,PORT)
DISCONNECT_MESSAGE="!DISCONNECT"

client.connect(Addr)
def send(msg):
    message=msg.encode(format)
    msg_length=len(message)
    send_length=str(msg_length).encode(format)
    send_length+=b' '*(header-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(format))
send(f"Here is my address {Addr} {Cname}")

def receive_file(filename,client):
    with open(filename, 'wb') as filepath:
        print("\nfile Created")
        done=False
        while not done:
            data=client.recv(1024)
            if data[-6:] == b"<DONE>":
                done=True
                filepath.write(data[:-6])
            else:
                filepath.write(data)
        print("\nfile received")

receive_file("update.bat", client)
client.close()
print("Socket closed. Exit the program")

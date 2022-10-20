import socket as soc
import threading
import sys

FORMAT = 'utf-8'
HEADER = 64
PORT = 5555
SERVER = soc.gethostbyname(soc.gethostname())
ADDR = (SERVER, PORT)
u_SOCKET = soc.socket(soc.AF_INET, soc.SOCK_STREAM)

DISSCONNECT_MSG = "Dissconnected!"

u_SOCKET.bind(ADDR)

def handle_client(conn, addr):
    print(f"New conncetion {addr} connected")
    connected = True
    while True:
        msgLen = conn.recv(HEADER).decode(FORMAT)
        if msgLen:
            msgLen = int(msgLen)
            msg = conn.recv(msgLen).decode(FORMAT)
            print(f"add= {addr} msg = {msg}")
        
            if msg == DISSCONNECT_MSG:
                connected = False
                print(DISSCONNECT_MSG)
                break
        
    conn.close()
        
        

def start():
    u_SOCKET.listen()
    print(f"Looking for connections... {SERVER}")
    while True:
        conn, addr = u_SOCKET.accept()
        thread = threading.Thread(target = handle_client, args= (conn, addr))
        thread.start()
        print(f"Active connections: {threading.active_count()-1}")
print("starting server...")
start()
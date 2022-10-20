import socket as soc

class client:
    
    def __init__(self) -> None:
        self.DISSCONNECT_MSG = "Dissconnected!"
        self.FORMAT = 'utf-8'
        self.HEADER = 64
        self.PORT = 5555
        self.SERVER = soc.gethostbyname(soc.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.u_client = soc.socket(soc.AF_INET, soc.SOCK_STREAM)     
        self.u_client.connect(self.ADDR)

    def send(self, msg):
        message = msg.encode(self.FORMAT)
        msgLen = len(message)
        send_len = str(msgLen).encode(self.FORMAT)
        send_len += b' ' * (self.HEADER-len(send_len))
        self.u_client.send(send_len)
        self.u_client.send(message)

client_obj = client()

client_obj.send("Hello world!")
#send(str(main.BUTTON_H))
input()
client_obj.send(client_obj.DISSCONNECT_MSG)
    
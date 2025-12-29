import socket,threading
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
_ip = config["server"]["host"]
port = int(config["server"]["port"])
no_of_client=int(config["server"]["max_clients"])
payload=""
indica="+"
def reciver(con,addr):
    temp="-"
    while True:
        if temp!=indica:
            try:
                con.send(payload.encode())
            except:
                con.close()
                break
            temp=indica
def sender(con,addr):
    def data(total_size,con):
        mes=""
        while True:
            try:
                data=con.recv(total_size).decode()
            except:
                return ""
            if data=="":
                con.close()
                return ""
            mes=mes+data
            n=len(mes)
            if n==total_size:
                return mes
            total_size=total_size-n
    global payload
    global indica
    close=1
    user_size=data(2,con)
    if user_size=="":
        close=0
    message=data(int(user_size),con)
    if message=="":
        close=0
    client_name=message
    if(close):
        while True:
            size=data(5,con)
            if size=="":
                break
            message=data(int(size),con)
            if message=="":
                break
            if indica=="+":
               indica="-"
            else:
               indica="+"
            payload=user_size+client_name+size+message
s=socket.socket()
s.bind((_ip,port))
s.listen(no_of_client)
while True:
    con,add=s.accept()
    b=con.recv(1).decode()
    if b=="1":
        t=threading.Thread(target=sender,args=(con,add))
        t.start()
    else:
       t1= threading.Thread(target=reciver,args=(con,add))
       t1.start()

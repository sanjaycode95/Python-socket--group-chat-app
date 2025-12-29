import socket
def mess_construct(data_size,data):
    data_len=len(str(len(data)))
    if(data_len==data_size):
        return str(len(data))+data
    req_len=data_size-data_len
    return "0"*req_len+str(len(data))+data
def mess_extract(soc):
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
    len_username=data(2,soc)
    user_name=data(int(len_username),soc)
    len_message=data(5,soc)
    user_message=data(int(len_message),soc)
    formated_mes= "\nUser:"+user_name+"\nmessage:\n"+user_message
    return formated_mes
soc=socket.socket()
soc.connect(("127.0.0.1",5002))
print("choose your option:")
a=(input("Enter 1 or 0 Sender-1/reciver-0:"))
if (a=="1" or "0"):
    soc.send(a.encode())
    if(a=="1"):
        name=input("Enter your name (99):")
        soc.send(mess_construct(2,name).encode())
        while True:
            mess=input("Enter your message to send group chat:")
            soc.send(mess_construct(5,mess).encode())
    else:
        while True:
            print(mess_extract(soc))

import socket

client = socket.socket()
print('please input the ip')
ip = input()
print('please input the path')
path=int(input())
client.connect((ip,path))
while True:
    msg = input(">> ").strip()
    if len(msg) == 0:continue
    client.send( msg.encode("utf-8") )
    data = client.recv(1024)
    print(data.decode()) #命令执行结果
client.close()
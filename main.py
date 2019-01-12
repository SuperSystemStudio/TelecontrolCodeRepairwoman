import socket

client = socket.socket()
print('please input the ip')
ip = input('ip: ')
print('please input the path')
path=int(input("path: "))
client.connect((ip,path))
mod = 0
while True:
    if mod == 0:
        msg = input('[user#127.0.0.1] ').strip()
    elif mod == 1:
        msg = input('[root#127.0.0.1] ').strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)
    print(data.decode()) #命令执行结果
    if data == b'please input the password':
        password = input('password: ').strip()
        if len(password) == 0:
            continue
    client.send(password.encode("utf-8"))
    data = client.recv(1024)
    if data == b'now,you are root!':
        mod = 1
print('连接已断开')
time.sleep(3)
client.close()
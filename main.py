import os
import sys
import time
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created')
platform = sys.platform
# Connect
def Connect():
    print('Please enter the ip')
    ip = input()
    time.sleep(1)
    print('Please enter the host')
    host = input()
    remote_ip = socket.gethostbyname( host )
    s.connect((ip , host))
    message = 'Connect.'
    print('loading')
    s.sendall(message)
    print ('Message send successfully')
    main()
# main
def main():
    mode=0
    true=1
    while true == 1:
        print('Please enter the command')
        command = input()
        if command == 'su':
            if mode == 0:
                print('Please input password')
                password=input()
                if password == '10000':
                    print('welcome')
                    mode = 1
                    print('now,you are root')
            elif mode == 1:
                print('you are root')
            else:
                print('Password error!')
        elif command == 'stop':
            if mode == 0:
                sys.exit()
            elif mode == 1:
                os._exit()
        else:
            print(command,':no find the command')
            time.sleep(1)
Connect()
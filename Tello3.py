#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018
#test

import threading 
import socket
import sys
import time

#受け取った返信をデコードして表示する関数
def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            response = data.decode(encoding="utf-8")
            print(response)
            if response == 'ERROR' or response == 'error':
                control(sock, tello_address, 'land')
                control(sock, tello_address, 'end')
        except Exception:
            print ('\Exit\n')
            break

#コマンドを受け取って実行する関数
def control(sock, address, com, dis):
    if 'end' in com:
        print ('-----')
        sock.close()  
        sys.exit()
        
    # Send data
    command = com + " " + dis
    command = command.encode(encoding="utf-8") 
    sent = sock.sendto(command, tello_address)
            

#ここからメイン
#接続先を設定
host = ''
port = 9000
locaddr = (host,port)

#telloのアドレスを指定
tello_address = ('192.168.10.1', 8889)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(locaddr)

#受信スレッドの構築
recvThread = threading.Thread(target=recv)
recvThread.start()

#通信できているか確認するためにはじめにcommandを送る
#OKならば動作する
control(sock, tello_address, 'command')
time.sleep(5)
control(sock, tello_address, 'takeoff')
time.sleep(5)
control(sock, tello_address, 'right', '50')
time.sleep(5)
control(sock, tello_address, 'forward','300')
time.sleep(5)
control(sock, tello_address, 'left', '70')
time.sleep(5)
control(sock, tello_address, 'back', '300')
time.sleep(5)
control(sock, tello_address, 'right', '25')
time.sleep(5)
control(sock, tello_address, 'land')
time.sleep(5)
control(sock, tello_address, 'end')


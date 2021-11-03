import socket
import threading

SERVER = '192.168.56.1'
PORT = 4545

print("[+] Waiting to connect to the server...")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


def recieve():
    msg = client.recv(1024).decode('utf-8')
    if msg == "OFF":
        client.close()
    else:
        print(msg)

def send():
    msg = input(">>> ")
    if msg == "OFF":
        client.send(msg.encode('utf-8'))
        client.close()
    else:
        client.send(msg.encode('utf-8'))


while True:
    recieve_thread = threading.Thread(target=recieve)
    recieve_thread.start()
    
    send_thread = threading.Thread(target=send)
    send_thread.start()






# while True:
# recieve = threading.Thread(target=recieve)
# send = threading.Thread(target=send)
#     # recieve()
#     # send()
# recieve.start()
# send.start()

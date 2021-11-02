import socket
import threading

SERVER = '192.168.56.1'
PORT = 4545

print("[+] Waiting to connect to the server...")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

print(client.recv(1024).decode('utf-8'))

def recieve():
    message = client.recv(1024).decode('utf-8')
    print(f'Server: {message}')

def send():
    message = input("Me: ")
    client.send(message.encode('utf-8'))

# send = threading.Thread(target=send)
# recieve = threading.Thread(target=recieve)

while True:
    recieve()
    send()
    # send.start()
    # recieve.start()

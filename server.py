import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 4545

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()
print(f'[+] Server is listening on {PORT}...')

client, address = server.accept()
client.send(f'[+] Connection established with {HOST} on port {PORT}\n'.encode('utf-8'))

print(f'[+] Connected to {address[0]} on port {PORT}')

def send():
    message = input("Me: ")
    client.send(message.encode('utf-8'))

def recieve():
    message = client.recv(1024).decode('utf-8')
    print(f'Client: {message}')

# send = threading.Thread(target=send)
# recieve = threading.Thread(target=recieve)

while True:
    send()
    recieve()
    # send.start()
    # recieve.start()




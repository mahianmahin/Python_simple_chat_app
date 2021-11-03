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
    msg = input(">>> ")
    if msg == "OFF":
        client.send(msg.encode('utf-8'))
        client.close()
    else:
        client.send(msg.encode('utf-8'))

def recieve():
    msg = client.recv(1024).decode('utf-8')
    if msg == "OFF":
        client.close()
    else:
        print(msg)


while True:
    send_thread = threading.Thread(target=send)
    send_thread.start()
    
    recieve_thread = threading.Thread(target=recieve)
    recieve_thread.start()



# while True:
# recieve = threading.Thread(target=recieve)
# send = threading.Thread(target=send)
# send.start()
# recieve.start()
    # recieve()
    # send()




# import socket
# import threading

# nickname = input("Nickname: ")

# # HOST = socket.gethostbyname(socket.gethostname())
# HOST = '192.168.0.102'
# # HOST = '127.0.0.1'
# PORT = 4545

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((HOST, PORT))

# server.listen()
# print(f'[+] Server is listening with {HOST} on {PORT}...')

# client, address = server.accept()
# client.send(f'[+] Connection established with {HOST} on port {PORT}\n'.encode('utf-8'))

# print(f'[+] Connected to {address[0]} on port {PORT}\n')

# def send():
#     while True:
#         msg = input("")

#         if msg == "OFF":
#             client.send(msg.encode('utf-8'))
#             client.close()
#             break

#         else:
#             msg = f'{nickname}: ' + str(msg)
#             client.send(msg.encode('utf-8'))

# def recieve():
#     while True:
#         msg = client.recv(1024).decode('utf-8')
#         print(str(msg))


# send_thread = threading.Thread(target=send)
# send_thread.start()

# recieve_thread = threading.Thread(target=recieve)
# recieve_thread.start()





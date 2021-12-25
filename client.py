# import socket
# import threading

# nickname = input("Nickname: ")
# ip = input("Server Ip address >>> ")

# # SERVER = '35.173.69.207'
# SERVER = str(ip)
# # SERVER = '192.168.56.1'
# PORT = 4545

# print("[+] Waiting to connect to the server...")


# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((SERVER, PORT))

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


# recieve_thread = threading.Thread(target=recieve)
# recieve_thread.start()
    
# send_thread = threading.Thread(target=send)
# send_thread.start()

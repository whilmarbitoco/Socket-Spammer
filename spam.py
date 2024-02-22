import socket
import string
import random
import time
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.1.118", 9990))

client_socket.sendall("Hello\n".encode())

def main() -> None:
    send = ''
    while True:
        ascii = random.choice(string.ascii_letters)
        send += ascii
        print(send+"\n")
        client_socket.send((send+"\n").encode())
        time.sleep(0.5)





t1 = threading.Thread(target=main)
t1.start()

t2 = threading.Thread(target=main)
t2.start()



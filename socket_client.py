# socket client creation
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # assign the server
    s.connect(('192.168.3.1', 50007))
    # send the message to server
    s.sendall(b'hello')
    # set network buffer size as 1024, get string from server
    data = s.recv(1024)
    #
    print(repr(data))

# socket server creation
import socket

# AF = IPv4
# if TCP/IP, then use SOCK_STREAM
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # assign IP address and port
    s.bind(('192.168.3.31', 50007))
    # 1 connection
    s.listen(1)
    # waiting for connection
    while True:
        # if anyone try to connect, input the connection and address
        conn, addr = s.accept()
        with conn:
            while True:
                # receive the data
                data = conn.recv(1024)
                if not data:
                    break
                print('data : {}, addr: {}'.format(data, addr))
                # return the data to client, here, "b -> byte" is necessary
                conn.sendall(b'Received: ' + data)

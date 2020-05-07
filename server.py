import socket

sock = socket.socket()
sock.bind(('',9090))
sock.listen(20)


clients  = []

conn, addr = sock.accept()

qqq=False
while not qqq:

    while True :
        data = conn.recv(1024)
        if data :
            break



    conn.send('{} {}'.format(addr, data).encode())

    def exit ():
        qqq = True

    print(addr)
conn.close()
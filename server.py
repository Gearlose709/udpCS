import socket

sock = socket.socket()
sock.bind(('',9090))
sock.listen(2)


clients  = []



qqq=False
while not qqq:
    conn, addr = sock.accept()
    while True :
        data = conn.recv(1024)
        if data :
            break

    if addr not in clients :
        clients.append(addr)
        conn.send('{} {}'.format(addr,data).encode())
    else:
        conn.send('{} {}'.format(addr, data).encode())

    def exit ():
        qqq = True

    print(addr)
conn.close()
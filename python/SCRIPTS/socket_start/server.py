from convert import *
import socket
import os

def server_program():
    
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print('Connection from: ' + str(address))
    while True:
        
        data = conn.recv(1024).decode()
        if not data:
            break

        print('User enter: ' + str(data))

        if data in ['help','h','helpme']:
            conn.send(str('All apps: '+','.join(conv.keys())).encode())
            pass

        try:
            print(conv[str(data)])
            os.system('start '+conv[str(data)])
        except KeyError:
            conn.send('App not found! for apps enter "help"'.encode())

    conn.close()


if __name__ == '__main__':
    server_program()
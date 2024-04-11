import socket

def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12345))
        s.sendall(b'Hello, world')
        data = s.recv(1024)
    print('Received', repr(data))

if __name__ == "__main__":
    client()
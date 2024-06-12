import socket


class SocketManager:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None

    def __enter__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        return self.socket

    def __exit__(self, exc_type, exc_value, traceback):
        self.socket.close()

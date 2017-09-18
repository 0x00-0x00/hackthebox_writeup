import socket

class SockClient(object):
    def __init__(self, dest="127.0.0.1", port=1, bufsize=8096, timeout=30, verbose=False):
        """
        Very simple socket operations
        """
        self.dest = dest
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bufsize = bufsize
        self.sock.settimeout(timeout)
        self.verbose = verbose

        # Check default port value
        if port == 1:
            print("Port is not set!")

        if self.verbose:
            print("New socket client created")
        if self.verbose:
            print("Trying to connect to destination: %s" % dest)

        try:
            self.sock.connect((dest.__str__(), port))
            if self.verbose:
                print("Connected to destination.")
        except Exception as e:
            print("print: {0}".format(e))

    def send(self, data):
        try:
            if type(data) == str:
                data = data.encode()
            return self.sock.send(data)
        except Exception as e:
            print("Socket print: {0}".format(e))

    def recv(self):
        try:
            data = self.sock.recv(self.bufsize)
            if type(data) == bytes:
                data = data.decode()
            return data
        except Exception as e:
            print("Socket print: {0}".format(e))



import socket, threading, logging, time
from debug import debug_setup

PORT = 7777
HOST = '127.0.0.1'
sending_data = 'hello'

debug_setup()
 
class Client(threading.Thread):

    def run(self):
        Client.run_client(HOST, PORT, sending_data)
        return

    def run_client(HOST, PORT, sending_data):

        logging.debug('CLIENT STARTED')

        client_sock = socket.socket()
        client_sock.connect((HOST, PORT))
        logging.debug('CLIENT CONNECTED')
        enter_data_inbytes = bytes(sending_data, 'utf-8')

        client_sock.sendall(enter_data_inbytes)

        client_sock.close()
        logging.debug('CLIENT CLOSED')

if __name__ == '__main__':
    Client.run_client(HOST, PORT, sending_data)
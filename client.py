import socket, threading, logging, time
from debug import debug_setup

PORT = 7777
HOST = '127.0.0.1'
# sending_data = 'hello'

debug_setup()
 
class Client(threading.Thread):

    def run(self):
        Client.run_client(HOST, PORT)
        return

    def run_client(HOST, PORT):

        logging.debug('CLIENT STARTED')

        file2 = open("client_input.txt","r")
        sending_data = file2.read()
        
        client_sock = socket.socket()
        client_sock.connect((HOST, PORT))
        logging.debug('CLIENT CONNECTED')
        enter_data_inbytes = bytes(sending_data, 'utf-8')

        client_sock.sendall(enter_data_inbytes)
        file2.close()

        client_sock.close()
        logging.debug('CLIENT CLOSED')

if __name__ == '__main__':
    Client.run_client(HOST, PORT)
import socket, threading, logging, sys

PORT = 7777
HOST = '127.0.0.1'
 
class Client(threading.Thread):

    def run(self):
        Client.run_client(HOST, PORT)
        return

    def run_client(HOST, PORT):

        logging.debug('CLIENT STARTED')

        file2 = open("client_input.txt","r")
        sending_data = file2.read()
        
        try:
            client_sock = socket.socket()
            client_sock.connect((HOST, PORT))
        except:
            print("Could not make a connection to the server")
            print("Press enter to quit")
            sys.exit(0)

        logging.debug('CLIENT CONNECTED')
        enter_data_inbytes = bytes(sending_data, 'utf-8')

        client_sock.sendall(enter_data_inbytes)
        file2.close()

        client_sock.close()
        logging.debug('CLIENT CLOSED')

if __name__ == '__main__':
    Client.run_client(HOST, PORT)
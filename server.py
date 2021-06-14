import socket, threading, logging, time
from debug import debug_setup

PORT = 7777
HOST = '127.0.0.1'

debug_setup()

class Server(threading.Thread):

    def run(self):
        logging.debug('*'*60)
        Server.run_server(HOST, PORT)
        logging.debug('*'*60)
        return

    def run_server(HOST, PORT):
        logging.debug('SERVER STARTED')
        file = open("server_output.txt","w")

        server_sock = socket.socket()
        server_sock.bind((HOST, PORT))
        server_sock.listen(0)

        logging.debug('SERVER WAITING FOR CONNECTION')
        
        conn, addr = server_sock.accept()

        print(conn, addr)

        with conn:
            logging.debug('Connected by %s', addr)
            while True:
                data = conn.recv(3000000)
                decoded_data = data.decode('UTF-8')

                logging.debug('Server got from client: %s ', decoded_data[:100])
                file.write(str(decoded_data))
                file.close()

                if not data:
                    break
                # conn.sendall(data)
                break
            
        server_sock.close()
        logging.debug('SERVER CLOSED')

        return decoded_data
    
if __name__ == '__main__':
    Server.run_server(HOST, PORT)
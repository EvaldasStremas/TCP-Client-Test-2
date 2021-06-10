# python -m unittest test.ServerTestCase
# python -m unittest test.ServerTestCase2

import socket, threading, unittest, logging, sys

PORT = 7777
HOST = '127.0.0.1'


logging.basicConfig(
    level=logging.DEBUG,
    # filename='app.log',
    # filemode='w',
    format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


class ServerTestCase(unittest.TestCase):

    def run_server(self):
        logging.debug('SERVER STARTED')
        global decoded_data

        server_sock = socket.socket()
        server_sock.bind((HOST, PORT))
        server_sock.listen(0)

        conn, addr = server_sock.accept()

        with conn:
            logging.debug('Connected by %s', addr)
            while True:
                data = conn.recv(3000000)
                decoded_data = data.decode('UTF-8')

                logging.debug('Server got: %s ', decoded_data)

                if not data:
                    break
                conn.sendall(data)
                break

        server_sock.close()
        logging.debug('SERVER CLOSED')
  

    def run_client(self, enter_data):
        logging.debug('CLIENT STARTED')
        logging.debug('Client sent: %s ', enter_data)

        client_sock = socket.socket()
        client_sock.connect((HOST, PORT))
        enter_data_inbytes = bytes(enter_data, 'utf-8')

        client_sock.sendall(enter_data_inbytes)
        client_sock.close()
        logging.debug('CLIENT CLOSED')


    def test_send_hello_string_to_server(self):
        logging.debug('***STARTED SINGLE STRING TO SERVER TEST***')
        
        enter_data = 'hello'

        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

        client_thread = threading.Thread(target=self.run_client(enter_data))
        client_thread.start()

        server_thread.join()
        client_thread.join()

        self.assertEqual(enter_data, decoded_data)


    def test_send_2mb_txt_file_to_server(self):
        logging.debug('***STARTED 2MB TXT FILE TO SERVER TEST***')

        f = open("random-text.txt", "r")
        # f = open("2mb-random-text.txt", "r")
        enter_data = f.read()
        f.close()

        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

        client_thread = threading.Thread(target=self.run_client(enter_data))
        client_thread.start()

        server_thread.join()
        client_thread.join()

        self.assertEqual(enter_data, decoded_data)
    

    def test_symbols(self):
        logging.debug('***STARTED SYMBOLS TO SERVER COMPATIBILITY TEST***')

        result_list = []
        data_list = (['','/', '*', '-','+','=','.',',',':',';','[',']','{','}','(',')',
        '!','@','#','$','%','^','&'])

        for enter_data in data_list:

            server_thread = threading.Thread(target=self.run_server)
            server_thread.start()

            client_thread = threading.Thread(target=self.run_client(enter_data))
            client_thread.start()

            server_thread.join()
            client_thread.join()

            result_list.append(decoded_data)
        
        self.assertEqual(data_list, result_list)

class ServerTestCase2(unittest.TestCase):

    def run_server(self):
        logging.debug('SERVER STARTED')
        global decoded_data

        server_sock = socket.socket()
        server_sock.bind((HOST, PORT))
        server_sock.listen(0)

        conn, addr = server_sock.accept()

        with conn:
            logging.debug('Connected by %s', addr)
            while True:
                data = conn.recv(3000000)
                decoded_data = data.decode('UTF-8')

                logging.debug('Server got: %s ', decoded_data)

                if not data:
                    break
                conn.sendall(data)
                break

        server_sock.close()
        logging.debug('SERVER CLOSED')
  

    def run_client(self, enter_data):
        logging.debug('CLIENT STARTED')
        logging.debug('Client sent: %s ', enter_data)

        client_sock = socket.socket()
        client_sock.connect((HOST, PORT))
        enter_data_inbytes = bytes(enter_data, 'utf-8')

        client_sock.sendall(enter_data_inbytes)
        client_sock.close()
        logging.debug('CLIENT CLOSED')


    def test_send_2mb_txt_file_to_server(self):
        logging.debug('***STARTED 2MB TXT FILE TO SERVER TEST***')

        # f = open("random-text.txt", "r")
        f = open("2mb-random-text.txt", "r")
        enter_data = f.read()
        f.close()

        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

        client_thread = threading.Thread(target=self.run_client(enter_data))
        client_thread.start()

        server_thread.join()
        client_thread.join()

        self.assertEqual(enter_data, decoded_data)
    

if __name__ == '__main__':
    unittest.main()

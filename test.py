import socket, threading, unittest, logging, sys
from logging.handlers import TimedRotatingFileHandler

PORT = 7777
HOST = '127.0.0.1'

logging.basicConfig(format='%(asctime)s %(filename)s %(levelname)s %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(filename)s %(levelname)s %(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(filename)s %(levelname)s %(message)s', level=logging.ERROR)

# FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
# LOG_FILE = "my_app.log"

FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "my_app.log"


def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(FORMATTER)
   return console_handler
def get_file_handler():
   file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
   file_handler.setFormatter(FORMATTER)
   return file_handler
def get_logger(logger_name):
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG) # better to have too much log than not enough
   logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler())
   # with this pattern, it's rarely necessary to propagate the error up to parent
   logger.propagate = False
   return logger

class ServerTestCase(unittest.TestCase):

    def run_server(self):
        global decoded_data

        server_sock = socket.socket()
        server_sock.bind((HOST, PORT))
        server_sock.listen(0)

        conn, addr = server_sock.accept()

        with conn:
            # print('Connected by', addr)
            while True:
                data = conn.recv(3000000)
                decoded_data = data.decode('UTF-8')

                logging.debug('server got: %s', decoded_data)
                logging.debug('This will get logged')

                if not data:
                    break
                conn.sendall(data)
                break

        server_sock.close()
  

    def run_client(self, enter_data):
        client_sock = socket.socket()
        client_sock.connect((HOST, PORT))
        # enter_data = input("Enter some text: ")
        enter_data_inbytes = bytes(enter_data, 'utf-8')

        client_sock.sendall(enter_data_inbytes)
        client_sock.close()


    def test_send_hello_string_to_server(self):
        
        enter_data = 'hello'

        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

        client_thread = threading.Thread(target=self.run_client(enter_data))
        client_thread.start()

        server_thread.join()
        client_thread.join()

        self.assertEqual(enter_data, decoded_data)

        my_logger = get_logger("my module name")
        my_logger.debug("a debug message")


    def test_send_2mb_txt_file_to_server(self):
        
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


if __name__ == '__main__':
    unittest.main()

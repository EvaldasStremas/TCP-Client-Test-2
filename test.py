import socket, threading, unittest

PORT = 7777
HOST = '127.0.0.1'

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
                data = conn.recv(1024)
                decoded_data = data.decode('UTF-8')
                print('server got: ', decoded_data)

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


    def test_string_hello(self):

        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

        enter_data = 'hello'

        client_thread = threading.Thread(target=self.run_client(enter_data))
        client_thread.start()


        # server_thread.join()
        # client_thread.join()

        self.assertEqual(enter_data, decoded_data)

    def test_txt_file(self):

        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

        enter_data = 'hello'

        client_thread = threading.Thread(target=self.run_client(enter_data))
        client_thread.start()


        # server_thread.join()
        # client_thread.join()

        self.assertEqual(enter_data, decoded_data)


if __name__ == '__main__':
    unittest.main()

# python -m unittest test.ServerTestCase
# python -m unittest test.ServerTestCase2

import unittest, time
from server import *
from client import *
from debug import debug_setup

PORT = 7777
HOST = '127.0.0.1'

debug_setup()

class ServerTestCase(unittest.TestCase):

    def test_a(self):

        server_thread = Server()
        client_thread = Client()

        print(server_thread)

        server_thread.start()
        time.sleep(0.0001)
        client_thread.start()

        client_thread.join()
        server_thread.join()


    def test_b(self):

        server_thread = Server()
        client_thread = Client()

        print(server_thread)

        server_thread.start()
        time.sleep(0.0001)
        client_thread.start()

        client_thread.join()
        server_thread.join()


    def test_c(self):

        server_thread = Server()
        client_thread = Client()

        print(server_thread)

        server_thread.start()
        time.sleep(0.0001)
        client_thread.start()

        client_thread.join()
        server_thread.join()
        
if __name__ == '__main__':
    unittest.main()
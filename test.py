import unittest, time, numpy as np
from server import *
from client import *
from debug import *

PORT = 7777
HOST = '127.0.0.1'

debug_setup()

class BaseTest:
    def server_and_client_base_code():
        server_thread = Server()
        client_thread = Client()

        server_thread.start()
        time.sleep(0.0001)
        client_thread.start()

        client_thread.join()
        server_thread.join()

    def write_to_client_input_txt(test_input_text):
        file2 = open("client_input.txt","w")
        file2.write(test_input_text)
        file2.close()


class A_FirstTaskTest(unittest.TestCase):

    def test_send_hello_string_to_server(self):
        logging.debug('***STARTED *HELLO* STRING TO SERVER TEST***')

        test_input_text = "Hello"

        BaseTest.write_to_client_input_txt(test_input_text)
        file = open("server_output.txt","r")
        BaseTest.server_and_client_base_code()

        server_output_text = file.read()

        file.close()

        self.assertEqual(test_input_text, server_output_text)


class B_AdditionalTests(unittest.TestCase):

    def test_send_random_letters_2mb_txt_file_to_server(self):
        logging.debug('***STARTED 2MB TXT FILE TO SERVER COMAPRISON TEST***')

        file3 = open("2mb-random-text.txt","r")
        test_input_text = file3.read()
        file3.close()

        
        BaseTest.write_to_client_input_txt(str(test_input_text))
        BaseTest.server_and_client_base_code()

        file = open("server_output.txt","r")
        server_output_text = file.read()

        file.close()

        self.assertEqual(test_input_text, server_output_text)


    def test_symbols(self):
        logging.debug('***STARTED SYMBOLS TO SERVER COMPATIBILITY TEST***')

        symbols_array = (['','/', '*', '-','+','=','.',',',':',';','[',']','{','}','(',')',
        '!','@','#','$','%','^','&'])

        # symbols_array = (['部','★'])

        for test_input_text in symbols_array:

            BaseTest.write_to_client_input_txt(test_input_text)
            BaseTest.server_and_client_base_code()

            file = open("server_output.txt","r")
            server_output_text = file.read()
            file.close()

            self.assertEqual(test_input_text, server_output_text)


class C_ServerPerformaceTests(unittest.TestCase):

    def test_performace(self):
        logging.debug('***STARTED PERFORMACE TEST***')

        result = []
        test_input_text = "Hello"

        for _ in range(0,30):
            start_time = time.time()

            BaseTest.write_to_client_input_txt(test_input_text)

            file = open("server_output.txt","r")

            BaseTest.server_and_client_base_code()
            server_output_text = file.read()
            file.close()

            self.assertEqual(test_input_text, server_output_text)

            end_time = time.time()
            result.append(end_time - start_time)

        logging.debug('Maximum value of the array is %s', np.max(result))
        logging.debug('Average value of the array is %s', np.average(result))
        logging.debug('Minimum value of the array is %s', np.min(result))

        self.assertLessEqual(np.max(result), 0.03)


class D_ConnectionTests(unittest.TestCase):

    def test_client_connection_without_server(self):
        logging.debug('***STARTED CLIENT CONNECTION WITHOUT SERVER TEST***')

        client_thread = Client()
        client_thread.start()
        client_thread.join()

    def test_successful_connection_to_server(self):
        logging.debug('***STARTED SUCCESSFUL CONNECTION TO SERVER TEST***')

        BaseTest.server_and_client_base_code()


if __name__ == '__main__':
    unittest.main()

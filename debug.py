import logging

def debug_setup():

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler()
        ]
    )
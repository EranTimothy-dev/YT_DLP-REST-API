import logging

def create_logger():
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler('status.log')
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger




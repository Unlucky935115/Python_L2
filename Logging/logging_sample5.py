import logging
from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
log_filename = "execution_logs/logging_sample5_{}.log".format(current_time)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
formatter =  logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger= logging.getLogger("MyLogger")
logger.setLevel(level=logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)


file_handler= logging.FileHandler(log_filename)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def logging_function():
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

logging_function()

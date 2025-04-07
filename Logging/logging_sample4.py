#Script to redirect the logs to a file without displaying on the console

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt= '%Y - %m - %d %H:%M',
                    filename="execution_logs/file_logging.log",
                    filemode='w')

logging.debug("This is debug message.")
logging.info("This is info message.")
logging.warning("This is warning message.")
logging.error("This is error message.")
logging.critical("This is critical message.")

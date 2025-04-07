import logging
from loguru_sample1 import logs_sample
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("logging_sample1")
logger.debug("This is a DEBUG Message")
logger.info("This is a INFO Message")
logger.warning("This is a WARNING Message")
logger.error("This is a ERROR Message")
logger.critical("This is a CRITICAL Message\n")

logs_sample()


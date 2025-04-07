from loguru import logger
import time
import threading

def threading_function(name):
    logger.info("Thread Starting --> {}".format(name))
    time.sleep(5)
    logger.info("Thread Ended --> {}".format(name))

if __name__=='__main__':
    logger.info("MAIN: Before Creating the Thread.")
    x= threading.Thread(target=threading_function, args=("sample",), daemon=True)
    logger.info("MAIN: Thread Created and Before running the Thread.")
    x.start()
    logger.info("MAIN: Waiting for the thread to finish")
    #x.join()
    logger.info("MAIN: All done")

from loguru import logger
import time
import threading

def threading_sample2(name):
    logger.info("Starting the Thread --> {}".format(name))
    time.sleep(3)
    logger.info("Thread Finished --> {}".format(name))

if __name__=="__main__":
    threads_list=[]
    for index in range(3):
        logger.info(f"MAIN: Creating a thread {index} and starting.")
        x= threading.Thread(target=threading_sample2, args=(index,))
        threads_list.append(x)
        x.start()

    for index, threads in enumerate(threads_list):
        logger.info(f"MAIN: Before joining the thread --> {index}")
        x.join()
        logger.info(f"MAIN: Thread Finished --> {index}")

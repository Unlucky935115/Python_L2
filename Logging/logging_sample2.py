import logging, sys
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def division(a,b):
    try:
        logging.info(f"Calculating the division of {a} and {b}")
        c = a / b
        logging.info(f"Result of {a}/{b} division is {c}")
        return c
    except Exception as e:
        logging.error("Invalid division. Aborting Script")
        logging.critical(f"{str(e)}")
        sys.exit(1)

print(division(4, 0))
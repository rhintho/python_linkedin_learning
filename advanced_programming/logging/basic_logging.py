import logging


def main():
    logging.basicConfig(level=logging.DEBUG, filemode="w", filename="output.log")

    logging.debug("Das ist eine Debug-Nachricht")
    logging.info("Das ist eine Info-Nachricht")
    logging.warning("Das ist eine Warning-Nachricht")
    logging.error("Das ist eine Error-Nachricht")
    logging.critical("Das ist eine Critical-Nachricht")

    logging.info("Hier ist eine {} Variable und eine int: {}".format("string", 10))


if __name__ == "__main__":
    main()

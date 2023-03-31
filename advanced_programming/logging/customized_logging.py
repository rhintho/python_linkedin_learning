import logging

ext_data = {"user": "Ralph"}


def meine_protokoll_funktion():
    logging.debug("Das ist eine Debug-Level-Nachricht", extra=ext_data)


def main():
    fmt_str = "%(asctime)s: %(levelname)s: %(funcName)s Zeile:%(lineno)d User:%(user)s %(message)s"
    date_str = "%Y/%m/%d %I:%M:%S %p"
    logging.basicConfig(level=logging.DEBUG, filename="output.log", format=fmt_str, datefmt=date_str)

    logging.info("Das ist eine Info-Nachricht", extra=ext_data)
    logging.warning("Das ist eine Warning-Nachricht", extra=ext_data)
    meine_protokoll_funktion()


if __name__ == "__main__":
    main()

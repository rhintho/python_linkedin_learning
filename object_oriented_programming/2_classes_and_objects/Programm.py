from Kunde import *
from Konto import *


class Programm:
    def __init__(self):
        Programm.main()

    @staticmethod
    def main():
        print("Programm startet ...\n", "-" * 50)

        konto1 = Konto(1000, "Girokonto")
        kunde1 = Kunde("Hans", "Dampf", 42, "m", "Wosstraße 19, 39817 Bordow", konto1)
        del konto1
        print("-" * 50)
        print("Kontostand bei Beginn:\t", kunde1.konto.kontostand)
        kunde1.konto.einzahlen(120)
        print("Neuer Kontostand:\t\t", kunde1.konto.kontostand)

        print("-" * 50, "\nProgramm beendet.")


Programm()

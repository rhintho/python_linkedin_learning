from Kunde import *
from Konto import *


class BankProgramm:
    def __init__(self):
        BankProgramm.main()

    @classmethod
    def main(cls):
        konto1 = Konto(1000, "Girokonto")
        kunde1 = Kunde("Hans", "Dampf", 42, "m", "Burgweg 20, 19876 Schlosshausen", konto1)
        print("Kontostand bei Beginn:\t", kunde1.konto.get_kontostand())
        kunde1.konto.einzahlen(110)
        print("Neuer Kontostand:\t\t", kunde1.konto.get_kontostand())
        kunde1.konto.kontostand = -10
        print("Neuer Kontostand:\t\t", kunde1.konto.get_kontostand())


BankProgramm()

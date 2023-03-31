from Katze import *
from Vogel import *
from Hund import *


class Programm:
    def __init__(self):
        Programm.main()

    @staticmethod
    def main():
        katze = Katze(1, "Susi", "Berlin", "Sebastian")
        vogel = Vogel(3)
        hund = Hund(7)
        hund.lautgeben()
        hund.lautgeben("Wau!")
        katze.lautgeben()
        print(vogel.alter)


Programm()

from Ausnahme import *


class Programm:
    def __init__(self):
        Programm.main()

    @staticmethod
    def main():
        obj = Ausnahme()
        obj.rechne()


Programm()

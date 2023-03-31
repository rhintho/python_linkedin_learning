from Sauegetier import *


class Hund(Sauegetier):

    def __init__(self, alter):
        Sauegetier.__init__(self, alter)

    def bellen(self):
        print("Wuff!")

    def lautgeben(self):
        print("Wuff!")

    # def lautgeben(self, laut):    # Überladen von Methoden ist in Python nicht möglich
    #     print(laut)

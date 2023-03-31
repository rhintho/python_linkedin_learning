from Sauegetier import *
from Eigentuemer import *


class Katze(Sauegetier, Eigentuemer):
    def __init__(self, alter, name, wohnort, person):
        Sauegetier.__init__(self, alter)
        Eigentuemer.__init__(self, wohnort, person)
        self.__name = name

    def __get_name(self):
        return self.__name

    def miauen(self):
        print("Miau")

    def lautgeben(self):
        print("Miau")
        super().lautgeben()

    name = property(__get_name)

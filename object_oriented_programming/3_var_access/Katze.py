"""
Um Zugriffsmöglichkeiten weiter einzuschränken, werden Getter und Setter auf private gestellt
und dann mit Properties gearbeitet.
"""

class Katze:
    def __init__(self, alter):
        self.__alter = alter

    def __get_alter(self):
        return self.__alter

    def __set_alter(self, alter):
        self.__alter = alter

    alter = property(__get_alter, __set_alter)
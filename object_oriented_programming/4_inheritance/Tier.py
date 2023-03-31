class Tier:
    def __init__(self, alter):
        self.__alter = alter

    def __get_alter(self):
        return self.__alter

    def __set_alter(self, alter):
        self.__alter = alter

    def lautgeben(self):
        print("To override")

    alter = property(__get_alter, __set_alter)

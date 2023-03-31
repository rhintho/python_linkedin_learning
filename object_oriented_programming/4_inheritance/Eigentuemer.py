class Eigentuemer:
    def __init__(self, wohnort, person):
        self.__wohnort = wohnort
        self.__person = person

    def __get_wohnort(self):
        return self.__wohnort

    def __set_wohnort(self, wohnort):
        self.__wohnort = wohnort

    def __get_person(self):
        return self.__person

    def __set_person(self, person):
        self.__person = person

    wohnort = property(__get_wohnort, __set_wohnort)
    person = property(__get_person, __set_person)

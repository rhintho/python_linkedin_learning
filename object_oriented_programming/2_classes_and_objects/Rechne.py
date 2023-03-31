"""
Der Unterschied zwischen static und class-Methode ist, dass Klassen sich auf die Klassen beziehen. static-Methoden
werden annotiert, kennen aber keinen Kontext der Klasse und können den Zustand auch nicht verändern
"""

class Rechne:
    @staticmethod
    def addiere(a, b):
        return a + b

    @staticmethod
    def multipliziere(a, b):
        return a * b

    @staticmethod
    def punktrechnung():
        print(Rechne.multipliziere(21, 2))
        print(Rechne.addiere(21, 2))
        object = Rechne()
        print(object.addiere(5, 6))

    @classmethod
    def rechne(cls):
        print(cls.addiere(22, 22))
        print(Rechne.multipliziere(22, 20))
        cls.punktrechnung()
        obj = Rechne()
        print(obj.addiere(15, 6))

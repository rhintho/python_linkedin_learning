"""
Beispiel für eine Klassenvariable und -Methode. Diese Vorgehensweise bietet mehr Hinweise auf Verweise im
Gegensatz zu self bei den Instanzen.
"""


class Tier:
    anzahl = 0

    def __init__(self):
        Tier.anzahl += 1

    @classmethod
    def anzahl_tiere(cls):
        return cls.anzahl

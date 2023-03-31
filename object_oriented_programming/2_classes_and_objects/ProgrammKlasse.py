from Tier import *


class ProgrammKlasse:
    def __init__(self):
        ProgrammKlasse.main()

    def main():
        print("Anzahl der Tiere:", Tier.anzahl_tiere())
        susi = Tier()
        print("Anzahl der Tiere:", Tier.anzahl_tiere())
        strolch = Tier()
        print("Anzahl der Tiere:", Tier.anzahl_tiere())
        herb = Tier()
        print("Anzahl der Tiere am Ende (Abfrage für Klasse)", Tier.anzahl_tiere())
        print("Anzahl der Tiere am Ende (Abfrage für Instanz)", susi.anzahl_tiere())


ProgrammKlasse()

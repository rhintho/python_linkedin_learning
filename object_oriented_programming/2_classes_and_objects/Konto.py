class Konto:
    def __init__(self, kontostand, kontotyp):
        self.kontostand = kontostand
        self.kontotyp = kontotyp
        print("Objkekt", self, "wird erzeugt.")

    def einzahlen(self, betrag):
        self.kontostand += betrag

    def auszahlen(self, betrag):
        pass

    def __del__(self):
        print("Objekt", self, "wurde eliminiert.")

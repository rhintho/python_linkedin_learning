from Fehler import *

class Ausnahme:
    i = 0

    def rechne(self):
        while True:
            try:
                z1 = float(input("Bitte die erste Zahl eingeben:\n"))
                z2 = float(input("Bitte die zweite Zahl eingeben:\n"))
                erg = z1 / z2
                print(erg)

            except ValueError:
                print("Bitte nur eine numerische Zahl eingeben.")
            except ZeroDivisionError:  # man kann auch ein Tupel nehmen, und mehrere Exception in einer Behandlung anführen
                print("Durch die Zahl 0 kann man keine Division durchführen.")
            except BaseException:  # allgemeinere Exceptions sollten immer hinten stehen, um Unreachable Code zu vermeiden
                print("Bitte nur int oder float eingeben.")
            else:
                print("Wird ausgeführt, wenn keine Ausnahme auftritt.")
            finally:
                print("Die finally-Anweisung, wird immer ausgeführt.")
            if input("Ende mit q - weiter mit jeder anderen Taste: ") == "q":
                break
        print("Ende des Programms.")

    def verifiziere(self):
        while True:
            try:
                geheimzahl = int(input("Bitte Geheimzahl eingeben:\n"))
                if geheimzahl % 7 != 0:
                    self.i += 1
                else:
                    print("Zugang gestattet")
                    return
            except ValueError:
                print("Nur Zahlen einegeben")
                self.i += 1
            if self.i > 2:
                raise Fehler()
            if input("Ende mit q - weiter mit jeder anderen Taste: ") == "q":
                break

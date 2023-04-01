class Ausnahme2:
    def rechne(self):
        while True:
            try:
                z1 = float(input("Bitte die erste Zahl eingeben:\n"))
                z2 = float(input("Bitte die zweite Zahl eingeben:\n"))
                erg = z1 / z2
                print(erg)

            except (ValueError, ZeroDivisionError) as e:
                print(e.args[0], type(e), sep="\t:\t")
            if input("Ende mit q - weiter mit jeder anderen Taste: ") == "q":
                break

        print("Ende des Programms.")

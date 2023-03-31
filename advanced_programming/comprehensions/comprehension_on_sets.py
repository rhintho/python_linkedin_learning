"""
Mit Comprehensions kann man Operationen sequenziell für verschiedene Daten in Listen, Dicts und Sets vornehmen.
Hier das Beispiel für die Sets
"""


def main():
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    ftemps1 = [(t * 9/5) + 32 for t in ctemps]
    ftemps2 = {(t * 9/5) + 32 for t in ctemps}
    print(ftemps1)
    print(ftemps2)

    s_temp = "The quick brown fox jumped pver the lazy dog"
    chars = {c.upper() for c in s_temp if not c.isspace()}
    print(sorted(chars))



if __name__ == "__main__":
    main()

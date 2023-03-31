"""
Mit Comprehensions kann man Operationen sequenziell für verschiedene Daten in Listen, Dicts und Sets vornehmen.
Hier das Beispiel für die Listen
"""


def main():
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # klassischer Weg
    even_squared = list(map(lambda e: e ** 2, filter(lambda e: e > 4 and e < 16, evens)))
    print(even_squared)

    # Comprehensions
    even_squared = [e**2 for e in evens]
    print(even_squared)

    odds_squared = [e**2 for e in odds if e > 3 and e < 17]
    print(odds_squared)


if __name__ == "__main__":
    main()

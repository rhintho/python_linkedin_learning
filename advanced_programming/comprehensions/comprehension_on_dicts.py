"""
Mit Comprehensions kann man Operationen sequenziell für verschiedene Daten in Listen, Dicts und Sets vornehmen.
Hier das Beispiel für die Dicts
"""


def main():
    ctemps = [0, 12, 34, 100]
    # Temperatur in Dict für Celsius und Fahrenheit.
    temp_dict = {t: (t * 9/5) + 32 for t in ctemps}
    print(temp_dict)

    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}
    # team = team1.update(team2)        # ist möglich, verändert aber nur ein Dict von den beiden
    complete_team = {k:v for team in (team1, team2) for k,v in team.items()}
    print(complete_team)

if __name__ == "__main__":
    main()

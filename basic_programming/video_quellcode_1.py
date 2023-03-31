#!/usr/bin/python
a = 2
a = 5

# Das ist der Nachname der Person
name = "Meier"
# Das ist der Vorname der Person
vorname = "Hans"
# Dies ist das Alter der Person
alter = 42

'''
Das ist ein Kommentar über
mehrere Zeilen hinweg!
'''

name = input("Bitte den Nachnamen eingeben\n> ")
vorname = input("Bitte den Vornamen eingeben\n> ")
alter = input("Bitte das Alter in Jahren angeben\n>  ")

print(name, vorname, alter, sep=", ")

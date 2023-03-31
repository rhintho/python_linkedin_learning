# Verwenden von Iteratoren

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysGer = ["So", "Mo", "Di", "Mi", "Do", "Fr"]

# Iterator kreieren
i = iter(days)
print(next(i))
print(next(i))
print(next(i))

for m in days:
    print(m)

for m in range(len(days)):
    print(m + 1, days[m])

for i, m in enumerate(days, start=1):
    print(i, m)

for m in zip(days, daysGer):
    print(m)

for i,m in enumerate(zip(days, daysGer), start=1):      # Ausführung stoppt dann auch bei Freitag, ohne Fehler
    print(i, m[0], "=", m[1], "in German")

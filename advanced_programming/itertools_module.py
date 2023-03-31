import itertools

seq1 = ["Joe", "John", "Mike"]

vals = [10, 20, 30, 40, 50, 40, 30]

# Die ewige Wiederholung
cycle1 = itertools.cycle(seq1)

print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))

# Zähler erstellen
count1 = itertools.count(100, 10)
print(next(count1))
print(next(count1))
print(next(count1))
print(next(count1))
print(next(count1))

# Akkumuliert Werte in einer Liste
acc = itertools.accumulate(vals)
print(vals)
print(list(acc))

# Verketten von Werten
x = itertools.chain("ABC", "1234")
print(list(x))


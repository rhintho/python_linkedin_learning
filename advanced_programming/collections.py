# Namedtuple
import string

import collections

Point = collections.namedtuple("Point", "x y")
p1 = Point(10, 20)
p2 = Point(30, 40)
print(p1, p2)
print(p1.x)

p1 = p1._replace(x=100)
print(p1, "\n")

# defaultdicts
from collections import defaultdict

fruits = ["apple", "pear", "orange", "banana", "apple", "grape", "banana", "banana"]

fruitcounter = defaultdict(int)  # sinnvoll, wenn man nicht weiß, ob Daten vorhanden sind

for fruit in fruits:
    fruitcounter[fruit] += 1

for (k, v) in fruitcounter.items():
    print(k + ":", str(v))

# Counter
from collections import Counter

class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah", "Kevin", "James", "James", "Melanie", "Penny", "Steve"]
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank", "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

c1 = Counter(class1)
c2 = Counter(class2)

print(c1["James"])
print(sum(c1.values()), "Studenten in Klasse 1")

c1.update(class2)
print(sum(c1.values()), "Studenten in Klasse 1 & 2")

print(c1.most_common(3))

c1.subtract(class2)
print(c1.most_common(3))

print(c1 & c2)

# Ordered Dictionary
from collections import OrderedDict

sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
              ("Kings", (15, 15)), ("Chargers", (20, 10)), ("Jets", (16, 14)), ("Warriors", (25, 5))]

sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)  # Sortierung nach Anzahl der Gewinne

teams = OrderedDict(sortedTeams)
print(teams)

tm, wl = teams.popitem(False)
print("Top Team:", tm, wl)
print(teams)  # nach popitem() Element nicht mehr in Liste

for i, team in enumerate(teams, start=1):
    print(i, team)
    if i == 4:
        break

a = OrderedDict({"a": 1, "b": 2, "c": 3})
# b = OrderedDict({"a": 1, "b": 2, "c": 3})
# b = OrderedDict({"a": 1, "b": 4, "c": 3})
b = {"a": 1, "c": 3, "b": 2}        # beim normalen Dict wird die Reihenfolge nicht beachtet nur bei OrderedDict
print("Test auf Gleichheit", a == b)


# Deque // die doppelendige Warteschlange
d = collections.deque(string.ascii_lowercase)
print("Anzahl Elemente:", str(len(d)))
print(d)

for elem in d:
    print(elem.upper(), end=",")

d.pop()
d.popleft()
d.append(2)
d.appendleft(1)
print(d)

d.rotate()
print(d)

from enum import Enum, unique, auto


@unique  # mit unique müssen nicht nur die names sondern auch die values eindeutig sein
class Fruits(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    # PEACH = 1
    PEACH = auto()


print(Fruits.APPLE)
print(type(Fruits.APPLE))
print(repr(Fruits.APPLE))

print(Fruits.APPLE.name, Fruits.APPLE.value)
print(Fruits.PEACH.name, Fruits.PEACH.value)

myFruits = {}
myFruits[Fruits.BANANA] = "Come Mr. Tally-man"
print(myFruits)

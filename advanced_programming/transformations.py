# Transformationsfunktionen zum Sortieren, Filtern und Mappen von Sequenzen

def filterFunc(x):
    if x % 2 == 0:
        return False
    return True


def filterFunc2(x):
    if x.isupper():
        return False
    return True


def squareFunc(x):
    return x ** 2


def toGrade(x):
    if x >= 90:
        return "A"
    elif x >= 80 and x < 90:
        return "B"
    elif x >= 70 and x < 80:
        return "C"
    elif x >= 60 and x < 70:
        return "D"
    else:
        return "F"


nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
chars = "abcDeFGHiJklmnoP"
grades = (81, 89, 94, 78, 61, 66, 99, 74)

# Filter
odds = list(filter(filterFunc, nums))
print(odds)

squares = list(filter(filterFunc2, chars))
print(squares)

# Mapping
squares = list(map(squareFunc, nums))
print(squares)

# Sortieren
grades = sorted(grades)
print(grades)
letters = list(map(toGrade, grades))
print(letters)

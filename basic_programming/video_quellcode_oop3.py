class Lebewesen:
    alter = 42


class Mensch(Lebewesen):
    name = "Hans"

obj = Mensch()
print(obj.name)
print(obj.alter)
class Tier:
    def __init__(self, name, alter, typ):
        self.name = name
        self.typ = typ
        self.alter = alter

    def laut_geben(self, text):
        print(text)


obj = Tier("Herby", 6, "Katze")
print(obj.typ)
obj.laut_geben("Miau")

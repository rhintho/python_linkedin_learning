class Fehler(BaseException):
    def __init__(self):
        print("Ausnahme vom Typ", type(self), "wurde geworfen.")
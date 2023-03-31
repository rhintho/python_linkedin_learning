print(eval("2+3+5"))

a = 4  # Typ wird durch Duck-Typing zur Laufzeit zugewiesen
a_type = type(a)
print(a_type)
print(type(a_type))

# Datentypen, die keine Werte haben
nichts = None
wahr = True
unwahr = False

var1 = 4
var2 = 4.0
print(type(var1), type(var2))

var3 = 1.1e3
print(var3)
var4 = 1 + 4j  # komplexe Zahlen mit j als imaginären Teil zu verwenden
print(var4)

print(4 + 4 == 8 and 2 + 3 == 5)  # Verkettung von Bedingungen mit and und or


def aussen(b):
    a = 41

    def innen():
        c = 69
        print(a * b, c)

    innen()


aussen(12)

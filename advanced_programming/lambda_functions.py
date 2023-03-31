# Lambda-Funktionen kommen zum Einsatz, wenn man eine Referenz auf eine Funktion braucht
# und nur für sehr kleine Funktionen gedacht

def celsiusToFahrenheit(temp):
    return (temp * 9 / 5) + 32


def fahrenheitToCelsius(temp):
    return (temp - 32) * 5 / 9


ctemps = [0, 12, 34, 100]
ftemps = [32, 65, 100, 212]

print(list(map(fahrenheitToCelsius, ftemps)))
print(list(map(celsiusToFahrenheit, ctemps)))


print(list(map(lambda t : (t - 32) * 5 / 9, ftemps)))
print(list(map(lambda t : (t * 9 / 5) + 32, ctemps)))


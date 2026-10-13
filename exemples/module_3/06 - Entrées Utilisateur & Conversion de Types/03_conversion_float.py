"""
Exemple 3 — float()

float() sert aux nombres avec une partie décimale.
Le point est le séparateur décimal attendu par Python.
"""

prix = float("19.99")
note = float(100)
mesure = float("1.5e-3")

print(prix)
print(note)
print(mesure)

infini = float("inf")
pas_un_nombre = float("nan")

print("Infini :", infini)
print("NaN :", pas_un_nombre)

# float("19,99") provoquerait ValueError.

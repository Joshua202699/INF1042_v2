"""
Exemple 4 — Valeurs de retour
"""

def carre(x):
    return x ** 2


def addition(a, b):
    return a + b


n = 5
c = carre(n)
print("Le carré de", n, "est", c)

total = addition(10, 20) + carre(3)
print("10 + 20 + 3² =", total)

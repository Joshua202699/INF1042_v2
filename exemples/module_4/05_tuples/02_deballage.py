"""Déballer un tuple dans plusieurs variables."""
coordonnees = (4.5, 7.2)
x, y = coordonnees
print(f"X : {x}, Y : {y}")

# Python peut aussi échanger deux valeurs par déballage.
a, b = 10, 5
print("Avant échange :", a, b)
a, b = b, a
print("Après échange :", a, b)

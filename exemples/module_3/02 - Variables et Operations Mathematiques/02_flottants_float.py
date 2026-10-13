"""
Exemple 2 — Flottants (float)

Les float représentent des nombres avec une partie décimale.
Python utilise le POINT comme séparateur décimal.
"""

temperature = 21.5
prix = 3.99
taux_taxe = 0.13

prix_total = prix * (1 + taux_taxe)

print("Température :", temperature)
print("Prix avant taxe :", prix)
print("Prix total brut :", prix_total)
print("Prix total arrondi :", round(prix_total, 2))
print(f"Prix total formaté : {prix_total:.2f} $")

# Les float sont stockés en binaire et certaines valeurs
# ne peuvent pas être représentées exactement.
print("0.1 + 0.2 =", 0.1 + 0.2)

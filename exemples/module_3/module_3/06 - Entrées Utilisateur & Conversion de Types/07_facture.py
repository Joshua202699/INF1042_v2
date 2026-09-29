"""
Exemple 7 — Calculateur de facture

Combine :
- input()
- str, int et float
- calculs
- f-strings
- méthodes de chaînes
"""

article = input("Nom du produit : ").strip()
quantite = int(input("Quantité achetée : "))
prix_unitaire = float(input("Prix unitaire ($) : "))

sous_total = quantite * prix_unitaire
taxe = sous_total * 0.13
total = sous_total + taxe

nb_caracteres = len(article)

print()
print(f"Article ({nb_caracteres} caractères) : {article.upper()}")
print(f"Sous-total : {sous_total:.2f} $")
print(f"Taxe : {taxe:.2f} $")
print(f"Total à payer : {total:.2f} $")

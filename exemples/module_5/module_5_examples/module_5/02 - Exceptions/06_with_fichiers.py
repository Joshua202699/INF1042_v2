"""
Exemple 6 — Gestionnaire de contexte with

with ferme automatiquement le fichier après le bloc,
même si une erreur se produit.
"""

from pathlib import Path

chemin = Path(__file__).with_name("data.txt")

# Écriture d'un petit fichier de démonstration.
with open(chemin, "w", encoding="utf-8") as fichier:
    fichier.write("Ligne 1\n")
    fichier.write("Ligne 2\n")

# Lecture sécuritaire du fichier.
with open(chemin, "r", encoding="utf-8") as fichier:
    contenu = fichier.read()

print("Contenu du fichier :")
print(contenu)
print("Le fichier est maintenant fermé automatiquement.")

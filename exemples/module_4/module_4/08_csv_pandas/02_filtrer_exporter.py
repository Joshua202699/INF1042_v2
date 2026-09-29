"""Filtrer un DataFrame puis exporter le résultat dans un nouveau CSV."""
import pandas as pd

df = pd.read_csv("joueurs.csv")

# Le masque est une série de True/False, une valeur par ligne.
masque = df["ppg"] < 5
low_scorers = df[masque]

print("Joueurs avec moins de 5 points par match :")
print(low_scorers)

# index=False évite d'écrire l'index pandas dans le fichier.
low_scorers.to_csv("low_scorers.csv", index=False)
print("\nFichier créé : low_scorers.csv")

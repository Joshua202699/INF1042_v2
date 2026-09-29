"""Lire un fichier CSV avec pandas et examiner les premières lignes."""
import pandas as pd

# Le fichier joueurs.csv doit être dans le même dossier que ce script.
df = pd.read_csv("joueurs.csv")

print("Les 5 premières lignes :")
print(df.head(5))
print("\nColonnes :", list(df.columns))
print("Nombre de joueurs :", len(df))

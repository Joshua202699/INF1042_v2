"""Regrouper des données et calculer une moyenne avec groupby()."""
import pandas as pd

df = pd.read_csv("joueurs.csv")

# 1) Grouper les lignes selon la position.
# 2) Sélectionner la colonne salary.
# 3) Calculer la moyenne dans chaque groupe.
stats = df.groupby("position")["salary"].mean()

print("Salaire moyen par position :")
print(stats)

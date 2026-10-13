"""Lire un fichier CSV avec pandas et examiner les premières lignes."""
import pandas as pd

# Le fichier basket.csv doit être dans le même dossier que ce script.
import pandas as pd
df = pd.read_csv("basket.csv")
print("Shape: ", df.shape)   #cols & #rows
print("Head: \n", df.head(5))  #5 premier rangées
print("Info: \n", df.info())    #chaque colonne, type, # valeurs
print("Types: \n", df.dtypes)  #colonne, type
print("Tail: \n", df.tail(3))  #dernier 3 rangées

print("Colonnes : ", list(df.columns))
print("Nombre de joueurs :", len(df))

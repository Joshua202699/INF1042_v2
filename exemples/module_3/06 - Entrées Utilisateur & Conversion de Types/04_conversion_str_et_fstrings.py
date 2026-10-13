"""
Exemple 4 — str() et f-strings

str() transforme une valeur en texte.
Les f-strings sont souvent plus faciles à lire.
"""

score = 95

message = "Votre score est : " + str(score)
print(message)

statut = True
print("Booléen converti :", str(statut))

grand_nombre = 123456789
nb_chiffres = len(str(grand_nombre))
print("Nombre de chiffres :", nb_chiffres)

# Variante recommandée :
print(f"Votre score est : {score}")

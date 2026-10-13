"""Compter la fréquence des mots avec un dictionnaire."""

texte = "Le chat mange, le chat dort."

# Nettoyage simple : enlever quelques signes de ponctuation.
for ponctuation in ",.!":
    texte = texte.replace(ponctuation, "")

# lower() uniformise les majuscules/minuscules.
# split() transforme la phrase en liste de mots.
mots = texte.lower().split()

compte = {}
for mot in mots:
    # get(mot, 0) donne 0 si le mot n'existe pas encore.
    compte[mot] = compte.get(mot, 0) + 1

print("Mots :", mots)
print("Fréquences :", compte)

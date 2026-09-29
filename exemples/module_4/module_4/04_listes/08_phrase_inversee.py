"""Manipuler du texte en utilisant une liste de mots."""
phrase = "Le petit ordinateur triste"

mots = phrase.split()          # Phrase -> liste de mots
mots_inverses = mots[::-1]     # Nouvelle liste en ordre inverse
resultat = " ".join(mots_inverses)  # Liste -> chaîne de caractères

print("Phrase originale :", phrase)
print("Liste de mots :", mots)
print("Phrase inversée :", resultat)

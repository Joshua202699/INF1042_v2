"""Créer un histogramme simple avec un dictionnaire."""
mots = ["chat", "chien", "chat", "oiseau"]
compte = {}

for mot in mots:
    compte[mot] = compte.get(mot, 0) + 1

print("Mots :", mots)
print("Comptage :", compte)

for mot, nombre in compte.items():
    print(f"{mot} : {nombre} occurrence(s)")

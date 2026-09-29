"""
Exemple 6 — Appels imbriqués, strip() et conversions en cascade
"""

age = int(input("Votre âge : ").strip())
taille = float(input("Taille en mètres : ").strip())

print("Âge :", age)
print("Taille :", taille)

valeur_texte = "12.9"
valeur_int = int(float(valeur_texte))

print('"12.9" -> float -> int :', valeur_int)

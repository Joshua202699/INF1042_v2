"""
Exemple 5 — Portée des variables (scope)

Une variable locale existe dans la fonction où elle est créée.
Une variable globale est créée au niveau principal du fichier.
"""

valeur_globale = 100


def montrer_locale():
    valeur_locale = 42
    print("Dans la fonction :", valeur_locale)
    print("Globale lisible :", valeur_globale)


montrer_locale()

print("À l'extérieur, globale :", valeur_globale)

# Cette ligne provoquerait NameError :
# print(valeur_locale)

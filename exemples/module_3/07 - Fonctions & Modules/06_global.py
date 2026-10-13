"""
Exemple 6 — Mot-clé global

Le mot-clé global permet de modifier une variable globale
depuis l'intérieur d'une fonction.

Pour les débutants, il vaut généralement mieux préférer
des paramètres et des valeurs de retour lorsque possible.
"""

valeur = 100


def lire_globale():
    print("Valeur globale :", valeur)


def modifier_globale():
    global valeur
    valeur = valeur * 2


lire_globale()
modifier_globale()
lire_globale()

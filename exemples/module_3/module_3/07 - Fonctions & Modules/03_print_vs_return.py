"""
Exemple 3 — print() versus return

print() affiche une information.
return renvoie une valeur au code qui a appelé la fonction.
"""

def carre_affiche(x):
    print(x ** 2)


def carre_retourne(x):
    return x ** 2


print("Avec print() :")
resultat_1 = carre_affiche(5)
print("Valeur réellement retournée :", resultat_1)

print()

print("Avec return :")
resultat_2 = carre_retourne(5)
print("Valeur retournée :", resultat_2)
print("On peut la réutiliser :", resultat_2 + 10)

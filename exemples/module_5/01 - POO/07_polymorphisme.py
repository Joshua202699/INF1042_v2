"""
Exemple 7 — Polymorphisme

Polymorphisme : appeler la même méthode sur des objets différents.
Chaque objet répond à sa manière.
"""


class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        return "..."


class Chien(Animal):
    def parler(self):
        return "Wouf !"


class Robot:
    # Robot n'hérite pas de Animal, mais il a les mêmes méthodes attendues.
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        return "Bip bop."


def faire_parler(creature):
    # Duck typing : si l'objet a .nom et .parler(), on peut l'utiliser.
    print(creature.nom, "→", creature.parler())


liste = [Chien("Rex"), Animal("Mystère"), Robot("R2")]

for element in liste:
    faire_parler(element)

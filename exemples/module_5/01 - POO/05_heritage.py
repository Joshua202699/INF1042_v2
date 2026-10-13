"""
Exemple 5 — Héritage

Une classe enfant hérite des attributs et des méthodes d'une classe parent.
Cela évite de répéter le même code dans plusieurs classes semblables.
"""


class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        return "..."


class Chien(Animal):
    pass


c = Chien("Rex")

# Chien n'a pas défini __init__ ni parler(), mais il les hérite de Animal.
print(c.nom)
print(c.parler())
print("Type de c :", type(c))
print("Est-ce un Animal ?", isinstance(c, Animal))

"""
Exemple 6 — Redéfinition d'une méthode et super()

Override / redéfinition : une classe enfant remplace une méthode du parent.
super() permet d'appeler la version du parent.
"""


class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        return "..."


class Chien(Animal):
    def parler(self):
        return "Wouf !"


class ChienGuide(Chien):
    def parler(self):
        base = super().parler()  # appelle Chien.parler()
        return base + " (calme)"


class Chat(Animal):
    def parler(self):
        return "Meow !"


class Lion(Chat):
    def parler(self):
        return super().parler() + " (roar)"  # appelle Chat.parler()


animaux = [Animal("Mystère"), Chien("Rex"), ChienGuide("Max"), Chat("Minou"), Lion("Simba")]

for animal in animaux:
    print(animal.nom, "→", animal.parler())

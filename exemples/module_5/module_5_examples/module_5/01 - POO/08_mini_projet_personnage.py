"""
Exemple 8 — Mini-projet POO : personnage de jeu

Ce fichier combine classe, attributs, méthodes, encapsulation simple et héritage.
"""


class Personnage:
    def __init__(self, nom, points_de_vie=100):
        self.nom = nom
        self.points_de_vie = points_de_vie

    def est_vivant(self):
        return self.points_de_vie > 0

    def recevoir_degats(self, degats):
        self.points_de_vie -= degats
        if self.points_de_vie < 0:
            self.points_de_vie = 0

    def attaquer(self, cible):
        degats = 10
        cible.recevoir_degats(degats)
        print(f"{self.nom} attaque {cible.nom} pour {degats} dégâts.")


class Guerrier(Personnage):
    def attaquer(self, cible):
        degats = 18
        cible.recevoir_degats(degats)
        print(f"{self.nom} frappe fort {cible.nom} pour {degats} dégâts.")


heros = Guerrier("Alex")
monstre = Personnage("Blob", 50)

while heros.est_vivant() and monstre.est_vivant():
    heros.attaquer(monstre)
    print(f"Vie de {monstre.nom} : {monstre.points_de_vie}")

print("Combat terminé.")

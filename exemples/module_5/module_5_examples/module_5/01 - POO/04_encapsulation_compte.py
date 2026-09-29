"""
Exemple 4 — Encapsulation simple

Encapsulation : protéger l'état interne de l'objet.
En Python, _solde est une convention qui signifie : « usage interne ».
On passe par des méthodes pour contrôler les changements.
"""


class Compte:
    def __init__(self, solde=0):
        if solde < 0:
            raise ValueError("Le solde initial ne peut pas être négatif.")
        self._solde = solde

    def deposer(self, montant):
        if montant <= 0:
            print("Le dépôt doit être positif.")
            return
        self._solde += montant

    def retirer(self, montant):
        if montant <= 0:
            print("Le retrait doit être positif.")
        elif montant <= self._solde:
            self._solde -= montant
        else:
            print("Fonds insuffisants")

    def afficher_solde(self):
        print(f"Solde : {self._solde:.2f} $")


compte = Compte(100)
compte.afficher_solde()

compte.deposer(50)
compte.afficher_solde()

compte.retirer(30)
compte.afficher_solde()

compte.retirer(500)
compte.afficher_solde()

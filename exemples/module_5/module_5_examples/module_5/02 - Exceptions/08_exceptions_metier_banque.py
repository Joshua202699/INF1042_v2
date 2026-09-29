"""
Exemple 8 — Exceptions personnalisées / métier

Une exception métier décrit une règle de l'application.
Ici, les erreurs parlent le langage d'une banque.
"""


class BanqueError(Exception):
    """Classe mère pour les erreurs de banque."""
    pass


class SoldeInsuffisant(BanqueError):
    pass


class CompteBloque(BanqueError):
    pass


class Compte:
    def __init__(self, solde, bloque=False):
        self.solde = solde
        self.bloque = bloque

    def retirer(self, montant):
        if self.bloque:
            raise CompteBloque("Le compte est bloqué.")
        if montant > self.solde:
            raise SoldeInsuffisant("Solde trop bas.")
        self.solde -= montant
        return self.solde


compte = Compte(100)

for montant in [40, 80]:
    try:
        nouveau_solde = compte.retirer(montant)
        print(f"Retrait de {montant} $ réussi. Nouveau solde : {nouveau_solde} $")
    except BanqueError as erreur:
        print("Opération refusée :", erreur)

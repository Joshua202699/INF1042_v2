"""
Exemple 9 — Bibliothèque standard

Python fournit de nombreux modules prêts à utiliser.
"""

import math
import random
from datetime import date, timedelta

print("Pi :", math.pi)
print("Racine carrée de 16 :", math.sqrt(16))

nombre = random.randrange(0, 10)
print("Nombre pseudo-aléatoire entre 0 et 9 :", nombre)

aujourdhui = date.today()
dans_une_semaine = aujourdhui + timedelta(days=7)

print("Aujourd'hui :", aujourdhui)
print("Dans 7 jours :", dans_une_semaine)

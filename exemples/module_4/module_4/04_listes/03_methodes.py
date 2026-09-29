"""Méthodes principales pour ajouter et retirer des éléments."""
panier = ["pomme", "banane", "orange"]
print("Départ :", panier)

panier.append("poire")
print("append('poire') :", panier)

panier.insert(1, "kiwi")
print("insert(1, 'kiwi') :", panier)

panier.remove("banane")
print("remove('banane') :", panier)

dernier = panier.pop()
print("pop() a retiré :", dernier)
print("Final :", panier)

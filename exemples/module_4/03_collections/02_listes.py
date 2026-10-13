"""Exemple de liste : ajouter, insérer et retirer des éléments."""

fruits = ["pomme", "banane"]
print("Au départ :", fruits)

# append() ajoute un élément à la fin.
fruits.append("orange")
print("Après append :", fruits)

# insert(index, valeur) ajoute un élément à une position précise.
fruits.insert(1, "kiwi")
print("Après insert :", fruits)

# pop() enlève ET retourne un élément. Sans index, il enlève le dernier.
dernier = fruits.pop()
print("Élément retiré :", dernier)
print("Liste finale :", fruits)

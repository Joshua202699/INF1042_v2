choix = ["Pierre, Papier, Ciseaux"]
ordinateur = random.choice(choix)
utilisateur = input("Choisissez Pierre, Papier, ou Ciiseaux :")
if utilisateur == ordinateur:
    print("Égalité!")
else:
    print("choix différents!")
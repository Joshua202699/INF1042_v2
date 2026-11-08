age = int(input("Quel est votre age"))
if age < 13:
    print("Enfant")
elif age <= 17:
    print("Adolescent")
elif age <= 64:
    print("Adulte")
else:
    print("Aîné")
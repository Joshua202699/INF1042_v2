"""
Exemple 3 — and, or, not

and : toutes les conditions doivent être vraies
or  : au moins une condition doit être vraie
not : inverse True et False
"""

age = 19
a_un_permis = True
est_accompagne = False

print("Majeur ET permis :", age >= 18 and a_un_permis)
print("Permis OU accompagné :", a_un_permis or est_accompagne)
print("PAS accompagné :", not est_accompagne)

if age >= 18 and a_un_permis:
    print("Condition composée réussie.")

"""
Exemple 4 — /, // et %

/  : division normale
// : division entière (floor division)
%  : reste de la division
"""

a = 10
b = 4

print("10 / 4  =", a / b)
print("10 // 4 =", a // b)
print("10 % 4  =", a % b)

quotient = a // b
reste = a % b

# Relation fondamentale :
# dividende = quotient × diviseur + reste
verification = quotient * b + reste

print("Vérification :", a, "=", quotient, "*", b, "+", reste)
print("Résultat :", verification)

# Attention avec les nombres négatifs :
print("-10 // 4 =", -10 // 4)
print("-10 % 4  =", -10 % 4)

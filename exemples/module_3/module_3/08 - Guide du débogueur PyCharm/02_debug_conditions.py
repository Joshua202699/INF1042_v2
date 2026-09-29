"""
Deuxième exemple pour pratiquer les breakpoints conditionnels.

Placez un breakpoint sur la ligne du `print` dans la boucle
et utilisez une condition comme : score >= 30
"""

scores = [5, 12, 18, 27, 31, 45]

for index, score in enumerate(scores):
    statut = "réussite" if score >= 30 else "à améliorer"
    print(index, score, statut)

"""Analyser des enregistrements stockés dans des tuples imbriqués."""
matchs = (
    ("Tigres", "Lynx", 25, 18),
    ("Aigles", "Panthères", 22, 25),
)

for equipe1, equipe2, score1, score2 in matchs:
    if score1 > score2:
        gagnant = equipe1
    elif score2 > score1:
        gagnant = equipe2
    else:
        gagnant = "Match nul"

    print(f"{equipe1} {score1} - {score2} {equipe2} -> {gagnant}")

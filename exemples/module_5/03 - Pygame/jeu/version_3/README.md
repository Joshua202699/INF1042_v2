# Version 3 — Pièces chronométrées et lasers

Cette version est basée sur `version_2_multiple_coins_lasers`.

## Nouveautés

- Les pièces sont représentées par une classe `Coin` dans `coin.py`.
- Les pièces commencent vertes.
- Après 2 secondes, elles deviennent orange.
- Après 4 secondes, elles deviennent rouges.
- Après 5 secondes, une pièce disparaît et le score diminue de 5 points.
- Quand une pièce disparaît, une nouvelle pièce est ajoutée après 2 secondes.
- Le joueur peut ramasser une pièce en la touchant.
- Le joueur peut aussi détruire une pièce avec un laser.
- Ramasser ou détruire une pièce ajoute 1 point.
- Si le score descend sous 0, le joueur perd.
- Si le score atteint 20, le joueur gagne.

## Contrôles

- `W`, `A`, `S`, `D` : déplacer le joueur
- `Espace` : tirer un laser
- `Échap` : pause / reprendre
- `F1` : afficher / cacher les boîtes de collision
- `R` : recommencer après une victoire ou une défaite

## Lancer le projet

```bash
python -m pip install -r requirements.txt
python main.py
```

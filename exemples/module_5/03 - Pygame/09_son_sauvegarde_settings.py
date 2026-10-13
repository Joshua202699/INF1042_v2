"""
Exemple 9 — Settings et sauvegarde JSON

Cet exemple ne joue pas de son pour éviter de dépendre d'un fichier audio,
mais il montre comment structurer des réglages et sauvegarder un score.
"""

import json
from pathlib import Path

WIDTH = 960
FPS = 60
PLAYER_SPEED = 260

save_path = Path(__file__).with_name("save_data.json")

data = {
    "meilleur_score": 1200,
    "niveau_debloque": 3,
    "volume": 0.7,
}

with open(save_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

with open(save_path, "r", encoding="utf-8") as file:
    data_lue = json.load(file)

print("Réglages du jeu")
print("Largeur :", WIDTH)
print("FPS :", FPS)
print("Vitesse joueur :", PLAYER_SPEED)
print("Données sauvegardées :", data_lue)

# Exemple avec un vrai fichier son :
# sound = pygame.mixer.Sound("assets/sounds/jump.wav")
# sound.play()

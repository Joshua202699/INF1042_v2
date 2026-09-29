"""
Exemple 1 — Fenêtre Pygame minimale

Installer Pygame :
    pip install pygame

Exécuter ce fichier. Fermer la fenêtre avec le X.
"""

import pygame

WIDTH = 800
HEIGHT = 500
FPS = 60
TITLE = "Fenêtre Pygame minimale"
BACKGROUND_COLOR = (30, 30, 45)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(FPS) / 1000  # temps écoulé depuis la dernière image, en secondes

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()

pygame.quit()

"""
Exemple 2 — Arrière-plan défilant

On dessine deux copies côte à côte.
Quand la première sort de l'écran, on recommence à x = 0.
"""

import pygame

WIDTH, HEIGHT = 800, 400
FPS = 60
SCROLL_SPEED = 180

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arrière-plan défilant")
clock = pygame.time.Clock()

# Création d'un fond simple sans image externe.
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((20, 30, 60))
for x in range(0, WIDTH, 80):
    pygame.draw.rect(background, (35, 50, 90), (x, 0, 40, HEIGHT))
for x in range(40, WIDTH, 160):
    pygame.draw.circle(background, (255, 255, 170), (x, 80), 8)

bg_x = 0
running = True

while running:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bg_x -= SCROLL_SPEED * dt
    if bg_x <= -background.get_width():
        bg_x = 0

    screen.blit(background, (bg_x, 0))
    screen.blit(background, (bg_x + background.get_width(), 0))
    pygame.display.flip()

pygame.quit()

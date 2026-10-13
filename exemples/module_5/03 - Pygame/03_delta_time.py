"""
Exemple 3 — Delta time (dt)

La vitesse est exprimée en pixels par seconde.
Avec dt, le mouvement reste semblable même si les FPS changent.
"""

import pygame

WIDTH, HEIGHT = 800, 250
FPS = 60
SPEED = 300  # pixels par seconde

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Delta time")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

x = 0
running = True

while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += SPEED * dt
    if x > WIDTH:
        x = -40

    screen.fill((25, 25, 35))
    pygame.draw.rect(screen, (255, 200, 80), (round(x), 100, 40, 40))
    texte = font.render(f"dt = {dt:.4f} s | vitesse = {SPEED} px/s", True, (240, 240, 240))
    screen.blit(texte, (20, 20))
    pygame.display.flip()

pygame.quit()

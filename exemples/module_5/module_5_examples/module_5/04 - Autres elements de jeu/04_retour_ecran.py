"""
Exemple 4 — Retour à l'écran

Quand l'objet quitte complètement la gauche, il revient à droite.
"""

import pygame

WIDTH, HEIGHT = 800, 300
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retour à l'écran")
clock = pygame.time.Clock()

cloud = pygame.Rect(WIDTH, 120, 90, 40)
speed = 160
running = True

while running:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cloud.x -= speed * dt
    if cloud.right < 0:
        cloud.left = WIDTH

    screen.fill((90, 170, 230))
    pygame.draw.ellipse(screen, (255, 255, 255), cloud)
    pygame.display.flip()

pygame.quit()

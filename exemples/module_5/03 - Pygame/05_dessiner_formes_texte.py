"""
Exemple 5 — Dessiner des formes et du texte

Les formes simples sont parfaites pour prototyper un jeu
avant d'ajouter des images.
"""

import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Formes et texte")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

score = 0
coin = pygame.Rect(350, 220, 40, 40)
running = True

while running:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if coin.collidepoint(event.pos):
                score += 1

    screen.fill((18, 18, 28))
    pygame.draw.rect(screen, (255, 210, 60), coin, border_radius=8)
    pygame.draw.circle(screen, (100, 200, 255), (100, 200), 35)
    pygame.draw.line(screen, (255, 120, 120), (50, 400), (750, 400), 4)

    texte = font.render(f"Score : {score}", True, (240, 240, 240))
    screen.blit(texte, (20, 20))

    pygame.display.flip()

pygame.quit()

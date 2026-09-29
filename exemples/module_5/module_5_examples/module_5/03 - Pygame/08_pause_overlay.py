"""
Exemple 8 — Pause et overlay

Un menu pause peut être un état du jeu + une couche semi-transparente.
Appuyez sur ÉCHAP pour alterner entre jeu et pause.
"""

import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60


def draw_pause_overlay(screen, font):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    title = font.render("PAUSE", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2)))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pause")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 64)

player = pygame.Rect(100, 220, 50, 50)
paused = False
running = True

while running:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused

    if not paused:
        player.x += 120 * dt
        if player.left > WIDTH:
            player.right = 0

    screen.fill((25, 25, 38))
    pygame.draw.rect(screen, (80, 180, 255), player)
    if paused:
        draw_pause_overlay(screen, font)
    pygame.display.flip()

pygame.quit()

"""
Exemple 4 — Entrées clavier, souris et événements

KEYDOWN : action ponctuelle.
key.get_pressed() : mouvement continu.
mouse.get_pos() : position actuelle de la souris.
"""

import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Entrées clavier et souris")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 26)

player = pygame.Rect(350, 220, 50, 50)
show_mouse_circle = True
running = True

while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                show_mouse_circle = not show_mouse_circle

    keys = pygame.key.get_pressed()
    speed = 260
    if keys[pygame.K_a]: player.x -= speed * dt
    if keys[pygame.K_d]: player.x += speed * dt
    if keys[pygame.K_w]: player.y -= speed * dt
    if keys[pygame.K_s]: player.y += speed * dt

    mouse_x, mouse_y = pygame.mouse.get_pos()

    screen.fill((22, 25, 35))
    pygame.draw.rect(screen, (80, 180, 255), player)
    if show_mouse_circle:
        pygame.draw.circle(screen, (255, 120, 80), (mouse_x, mouse_y), 12)

    info = font.render("WASD pour bouger | ESPACE pour afficher/cacher le cercle", True, (240, 240, 240))
    screen.blit(info, (20, 20))
    pygame.display.flip()

pygame.quit()

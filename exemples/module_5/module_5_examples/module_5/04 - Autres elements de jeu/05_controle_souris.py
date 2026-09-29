"""
Exemple 5 — Contrôle à la souris

Position directe : l'objet se colle à la souris.
Mouvement fluide : l'objet se déplace vers la souris graduellement.
Appuyez sur ESPACE pour changer de mode.
"""

import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60
SPEED = 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Contrôle souris")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

rect = pygame.Rect(100, 100, 40, 40)
pos = pygame.Vector2(rect.center)
direct_mode = False
running = True

while running:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            direct_mode = not direct_mode

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if direct_mode:
        rect.center = (mouse_x, mouse_y)
        pos.update(rect.center)
    else:
        target = pygame.Vector2(mouse_x, mouse_y)
        direction = target - pos
        if direction.length() > 5:
            pos += direction.normalize() * SPEED * dt
        rect.center = (round(pos.x), round(pos.y))

    screen.fill((22, 25, 35))
    pygame.draw.rect(screen, (100, 220, 160), rect)
    mode = "direct" if direct_mode else "fluide"
    text = font.render(f"Mode : {mode} | ESPACE pour changer", True, (240, 240, 240))
    screen.blit(text, (20, 20))
    pygame.display.flip()

pygame.quit()

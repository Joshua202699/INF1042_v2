from pathlib import Path
import random
import sys

import pygame

from player import Player
from settings import (
    BACKGROUND_COLOR,
    COIN_COLOR,
    FPS,
    HEIGHT,
    HITBOX_COLOR,
    HUD_TEXT_COLOR,
    TITLE,
    WIDTH,
)

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "assets" / "images"


def draw_hud(screen, font, score, player):
    """Draw a transparent score panel in the top-right corner."""
    panel = pygame.Surface((220, 90), pygame.SRCALPHA)
    panel.fill((0, 0, 0, 140))
    screen.blit(panel, (WIDTH - 240, 20))

    score_text = font.render(f"Score : {score}", True, HUD_TEXT_COLOR)
    speed_text = font.render(f"Vitesse : {int(player.speed)}", True, HUD_TEXT_COLOR)
    help_text = font.render("WASD: bouger", True, HUD_TEXT_COLOR)

    screen.blit(score_text, (WIDTH - 220, 32))
    screen.blit(speed_text, (WIDTH - 220, 56))
    screen.blit(help_text, (WIDTH - 220, 80))


def draw_pause_overlay(screen, font):
    """Draw a semi-transparent pause screen."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    title = font.render("PAUSE", True, HUD_TEXT_COLOR)
    message = font.render("Appuie sur Échap pour reprendre", True, HUD_TEXT_COLOR)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
    screen.blit(message, message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))


def new_coin_rect():
    """Create a collectible rectangle at a random screen position."""
    return pygame.Rect(random.randint(40, WIDTH - 80), random.randint(40, HEIGHT - 80), 32, 32)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    player = Player(start_pos=(WIDTH // 2, HEIGHT // 2), image_folder=IMAGE_DIR)
    all_sprites = pygame.sprite.Group(player)

    coin_rect = new_coin_rect()
    score = 0
    running = True
    paused = False
    show_hitboxes = False

    while running:
        # Delta time keeps movement consistent even if FPS changes.
        dt = clock.tick(FPS) / 1000

        # 1) Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
                elif event.key == pygame.K_F1:
                    show_hitboxes = not show_hitboxes

        # 2) Update
        if not paused:
            keys = pygame.key.get_pressed()
            player.update(keys, dt, screen.get_rect())

            if player.rect.colliderect(coin_rect):
                score += 1
                coin_rect = new_coin_rect()

        # 3) Draw
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, COIN_COLOR, coin_rect, border_radius=8)
        all_sprites.draw(screen)
        draw_hud(screen, font, score, player)

        if show_hitboxes:
            pygame.draw.rect(screen, HITBOX_COLOR, coin_rect, 1)
            player.draw_hitbox(screen)

        if paused:
            draw_pause_overlay(screen, font)

        # 4) Display
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

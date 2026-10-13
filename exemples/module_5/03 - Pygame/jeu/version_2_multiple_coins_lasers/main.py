import random
import sys
from pathlib import Path

import pygame

from player import Player
from settings import (
    BACKGROUND_COLOR,
    COIN_COLOR,
    COIN_RESPAWN_DELAY,
    FPS,
    HEIGHT,
    HITBOX_COLOR,
    HUD_TEXT_COLOR,
    INITIAL_COIN_COUNT,
    LASER_COLOR,
    LASER_LENGTH,
    LASER_SPEED_MULTIPLIER,
    LASER_WIDTH,
    TITLE,
    WIDTH,
)

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "assets" / "images"


def draw_hud(screen, font, score, player, coin_count, laser_count):
    """Draw a transparent score panel in the top-right corner."""
    panel = pygame.Surface((270, 190), pygame.SRCALPHA)
    panel.fill((0, 0, 0, 140))
    screen.blit(panel, (WIDTH - 290, 20))

    score_text = font.render(f"Score : {score}", True, HUD_TEXT_COLOR)
    coin_text = font.render(f"Pièces : {coin_count}", True, HUD_TEXT_COLOR)
    laser_text = font.render(f"Lasers : {laser_count}", True, HUD_TEXT_COLOR)
    speed_text = font.render(f"Vitesse : {int(player.speed)}", True, HUD_TEXT_COLOR)
    help_text = font.render("WASD: bouger", True, HUD_TEXT_COLOR)
    shoot_text = font.render("Espace: laser", True, HUD_TEXT_COLOR)
    debug_text = font.render("F1: hitboxes", True, HUD_TEXT_COLOR)

    screen.blit(score_text, (WIDTH - 270, 36))
    screen.blit(coin_text, (WIDTH - 270, 60))
    screen.blit(laser_text, (WIDTH - 270, 84))
    screen.blit(speed_text, (WIDTH - 270, 108))
    screen.blit(help_text, (WIDTH - 270, 132))
    screen.blit(shoot_text, (WIDTH - 270, 156))
    screen.blit(debug_text, (WIDTH - 270, 180))


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
    """Create one collectible rectangle at a random screen position."""
    return pygame.Rect(
        random.randint(40, WIDTH - 80),
        random.randint(40, HEIGHT - 80),
        32,
        32,
    )


def create_laser(player):
    """Create a laser that starts at the player and travels in the aim direction."""
    return {
        "pos": pygame.math.Vector2(player.rect.center),
        "direction": player.aim_direction.copy(),
    }


def update_lasers(lasers, dt, screen_rect, laser_speed):
    """Move lasers forward and remove them when they leave the screen."""
    for laser in lasers[:]:
        laser["pos"] += laser["direction"] * laser_speed * dt

        if not screen_rect.collidepoint(laser["pos"]):
            lasers.remove(laser)


def draw_lasers(screen, lasers):
    """Draw each laser as a short line."""
    for laser in lasers:
        start = laser["pos"]
        end = start + laser["direction"] * LASER_LENGTH
        pygame.draw.line(screen, LASER_COLOR, start, end, LASER_WIDTH)


def update_coin_respawns(coins, pending_coin_spawns, dt):
    """Add a new coin 2 seconds after each collected coin."""
    for index in range(len(pending_coin_spawns) - 1, -1, -1):
        pending_coin_spawns[index] -= dt

        if pending_coin_spawns[index] <= 0:
            coins.append(new_coin_rect())
            pending_coin_spawns.pop(index)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)
    screen_rect = screen.get_rect()

    player = Player(start_pos=(WIDTH // 2, HEIGHT // 2), image_folder=IMAGE_DIR)
    all_sprites = pygame.sprite.Group(player)

    coins = [new_coin_rect() for _ in range(INITIAL_COIN_COUNT)]
    pending_coin_spawns = []
    lasers = []

    laser_speed = player.speed * LASER_SPEED_MULTIPLIER

    score = 0
    running = True
    paused = False
    show_hitboxes = False

    while running:
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

                elif event.key == pygame.K_SPACE and not paused:
                    lasers.append(create_laser(player))

        # 2) Update
        if not paused:
            keys = pygame.key.get_pressed()

            player.update(keys, dt, screen_rect)
            update_lasers(lasers, dt, screen_rect, laser_speed)
            update_coin_respawns(coins, pending_coin_spawns, dt)

            for coin in coins[:]:
                if player.rect.colliderect(coin):
                    score += 1
                    coins.remove(coin)
                    pending_coin_spawns.append(COIN_RESPAWN_DELAY)

        # 3) Draw
        screen.fill(BACKGROUND_COLOR)

        for coin in coins:
            pygame.draw.rect(screen, COIN_COLOR, coin, border_radius=8)

        draw_lasers(screen, lasers)

        all_sprites.draw(screen)
        draw_hud(screen, font, score, player, len(coins), len(lasers))

        if show_hitboxes:
            for coin in coins:
                pygame.draw.rect(screen, HITBOX_COLOR, coin, 1)

            player.draw_hitbox(screen)

        if paused:
            draw_pause_overlay(screen, font)

        # 4) Display
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

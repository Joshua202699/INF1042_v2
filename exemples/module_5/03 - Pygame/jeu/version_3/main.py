import sys
from pathlib import Path

import pygame

from coin import Coin
from player import Player
from settings import (
    BACKGROUND_COLOR,
    COIN_COLLECT_POINTS,
    COIN_EXPIRE_PENALTY,
    COIN_RESPAWN_DELAY,
    FPS,
    HEIGHT,
    HUD_TEXT_COLOR,
    INITIAL_COIN_COUNT,
    LASER_COLOR,
    LASER_LENGTH,
    LASER_SPEED_MULTIPLIER,
    LASER_WIDTH,
    TITLE,
    WIDTH,
    WINNING_SCORE,
)

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "assets" / "images"


def draw_hud(screen, font, score, player, coin_count, laser_count, game_state, niveau):
    """Draw a transparent score panel in the top-right corner."""
    panel = pygame.Surface((300, 215), pygame.SRCALPHA)
    panel.fill((0, 0, 0, 140))
    screen.blit(panel, (WIDTH - 320, 20))

    lines = [
        f"Score/Objectif : {score}/{WINNING_SCORE}",
        f"Pièces : {coin_count}",
        f"Lasers : {laser_count}",
        f"Niveau: {niveau}",
        f"Vitesse : {int(player.speed)}",
        f"État : {game_state}",
        "WASD: bouger",
        "Espace: laser",
        "F1: hitboxes",
    ]

    y = 36
    for line in lines:
        text = font.render(line, True, HUD_TEXT_COLOR)
        screen.blit(text, (WIDTH - 300, y))
        y += 22


def draw_pause_overlay(screen, font):
    """Draw a semi-transparent pause screen."""
    draw_center_overlay(
        screen,
        font,
        title="PAUSE",
        message="Appuie sur Échap pour reprendre",
    )


def draw_center_overlay(screen, font, title, message):
    """Draw a centered overlay for pause, win, and lose screens."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))

    title_font = pygame.font.SysFont(None, 64)
    title_image = title_font.render(title, True, HUD_TEXT_COLOR)
    message_image = font.render(message, True, HUD_TEXT_COLOR)
    restart_image = font.render("R: recommencer | Fermer la fenêtre pour quitter", True, HUD_TEXT_COLOR)

    screen.blit(title_image, title_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 55)))
    screen.blit(message_image, message_image.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    screen.blit(restart_image, restart_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40)))

def draw_niveau_overlay(screen, font, title, message):
    """Draw a centered overlay to advance to next level."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))

    title_font = pygame.font.SysFont(None, 64)
    title_image = title_font.render(title, True, HUD_TEXT_COLOR)
    message_image = font.render(message, True, HUD_TEXT_COLOR)
    restart_image = font.render("Appuie sur 'r' pour continuer au prochain niveau", True, HUD_TEXT_COLOR)

    screen.blit(title_image, title_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 55)))
    screen.blit(message_image, message_image.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    screen.blit(restart_image, restart_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40)))


def create_laser(player):
    """Create a laser that starts at the player and travels in the aim direction."""
    return {
        "pos": pygame.math.Vector2(player.rect.center),
        "direction": player.aim_direction.copy(),
    }


def laser_end(laser):
    """Return the end point of a laser line."""
    return laser["pos"] + laser["direction"] * LASER_LENGTH


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
        end = laser_end(laser)
        pygame.draw.line(screen, LASER_COLOR, start, end, LASER_WIDTH)


def laser_hits_coin(laser, coin):
    """Use Rect.clipline to test whether the laser line touches the coin."""
    start = laser["pos"]
    end = laser_end(laser)
    return coin.rect.clipline(start, end)


def update_coin_respawns(coins, pending_coin_spawns, dt):
    """Add a new coin 2 seconds after each deleted coin."""
    for index in range(len(pending_coin_spawns) - 1, -1, -1):
        pending_coin_spawns[index] -= dt

        if pending_coin_spawns[index] <= 0:
            coins.append(Coin.create_random())
            pending_coin_spawns.pop(index)


def reset_game(niveau):
    """Create the starting objects for a new game, or advance next level"""
    coins = [Coin.create_random() for _ in range(INITIAL_COIN_COUNT[niveau])]
    pending_coin_spawns = []
    lasers = []
    score = 0
    game_state = "playing"
    return coins, pending_coin_spawns, lasers, score, game_state


def check_end_conditions(score, niveau):
    """Return the current game state based on the score."""
    if score < 0:
        return "lost", niveau

    if score >= WINNING_SCORE:
        return "won", niveau + 1

    return "playing", niveau


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)
    screen_rect = screen.get_rect()

    player = Player(start_pos=(WIDTH // 2, HEIGHT // 2), image_folder=IMAGE_DIR)
    all_sprites = pygame.sprite.Group(player)

    niveau = 0
    coins, pending_coin_spawns, lasers, score, game_state = reset_game(niveau)
    laser_speed = player.speed * LASER_SPEED_MULTIPLIER

    running = True
    show_hitboxes = False


    while running:
        dt = clock.tick(FPS) / 1000

        # 1) Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and game_state in ("playing", "paused"):
                    game_state = "paused" if game_state == "playing" else "playing"

                elif event.key == pygame.K_F1:
                    show_hitboxes = not show_hitboxes

                elif event.key == pygame.K_SPACE and game_state == "playing":
                    lasers.append(create_laser(player))

                elif event.key == pygame.K_r and game_state == "lost":
                    player = Player(start_pos=(WIDTH // 2, HEIGHT // 2), image_folder=IMAGE_DIR)
                    all_sprites = pygame.sprite.Group(player)
                    coins, pending_coin_spawns, lasers, score, game_state = reset_game(0)
                    laser_speed = player.speed * LASER_SPEED_MULTIPLIER

                elif event.key == pygame.K_r and game_state == "won":
                    player = Player(start_pos=(WIDTH // 2, HEIGHT // 2), image_folder=IMAGE_DIR)
                    all_sprites = pygame.sprite.Group(player)
                    coins, pending_coin_spawns, lasers, score, game_state = reset_game(niveau)
                    laser_speed = player.speed * LASER_SPEED_MULTIPLIER
                    game_state = "playing"

        # 2) Update
        if game_state == "playing":
            keys = pygame.key.get_pressed()

            player.update(keys, dt, screen_rect)
            update_lasers(lasers, dt, screen_rect, laser_speed)
            update_coin_respawns(coins, pending_coin_spawns, dt)

            for coin in coins:
                coin.update(dt)

            # Player collecting coins
            for coin in coins[:]:
                if player.rect.colliderect(coin.rect):
                    score += coin.current_points(COIN_COLLECT_POINTS)
                    coins.remove(coin)
                    pending_coin_spawns.append(COIN_RESPAWN_DELAY)
                    game_state, niveau = check_end_conditions(score, niveau)

            # Lasers hitting coins
            if game_state == "playing":
                for laser in lasers[:]:
                    for coin in coins[:]:
                        if laser_hits_coin(laser, coin):
                            score += coin.current_points(COIN_COLLECT_POINTS)
                            coins.remove(coin)
                            pending_coin_spawns.append(COIN_RESPAWN_DELAY)
                            lasers.remove(laser)
                            game_state, niveau = check_end_conditions(score, niveau)
                            break

            # Coins expiring
            if game_state == "playing":
                for coin in coins[:]:
                    if coin.is_expired():
                        score -= COIN_EXPIRE_PENALTY
                        coins.remove(coin)
                        pending_coin_spawns.append(COIN_RESPAWN_DELAY)
                        game_state, niveau = check_end_conditions(score, niveau)

        # 3) Draw
        screen.fill(BACKGROUND_COLOR)

        for coin in coins:
            coin.draw(screen)

        draw_lasers(screen, lasers)
        all_sprites.draw(screen)
        draw_hud(screen, font, score, player, len(coins), len(lasers), game_state, niveau)

        if show_hitboxes:
            for coin in coins:
                coin.draw_hitbox(screen)

            player.draw_hitbox(screen)

        if game_state == "paused":
            draw_pause_overlay(screen, font)
        elif game_state == "won":
            draw_niveau_overlay(
                screen,
                font,
                title="GAGNÉ!",
                message=f"Tu as atteint {WINNING_SCORE} points.",
            )
        elif game_state == "lost":
            draw_center_overlay(
                screen,
                font,
                title="PERDU",
                message="Ton score est tombé sous zéro.",
            )

        # 4) Display
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

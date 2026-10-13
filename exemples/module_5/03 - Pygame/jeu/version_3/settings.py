"""Project constants for version 3 of the Pygame starter project."""

WIDTH = 960
HEIGHT = 540
FPS = 60

TITLE = "Pygame WASD Starter - Timed Coins and Lasers"

PLAYER_SPEED = 260  # pixels per second
PLAYER_SIZE = 96

INITIAL_COIN_COUNT = [3,4,5,6,7,8,9]
COIN_RESPAWN_DELAY = 2.0  # seconds
COIN_SIZE = 32
COIN_LIFETIME = 5.0  # seconds before the coin disappears
COIN_ORANGE_TIME = 2.0  # seconds before changing from green to orange
COIN_RED_TIME = 4.0  # seconds before changing from orange to red
COIN_COLLECT_POINTS = [3,2,1]
COIN_EXPIRE_PENALTY = 5
WINNING_SCORE = 15

LASER_LENGTH = 30
LASER_WIDTH = 4
LASER_SPEED_MULTIPLIER = 2

BACKGROUND_COLOR = (20, 24, 36)
HUD_TEXT_COLOR = (245, 247, 250)
COIN_GREEN = (57, 217, 138)
COIN_ORANGE = (255, 165, 0)
COIN_RED = (230, 57, 70)
LASER_COLOR = (255, 80, 80)
HITBOX_COLOR = (255, 255, 255)

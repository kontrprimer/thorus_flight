import pygame
from .framework import Vector2D


class Controls:
    UP = pygame.K_UP
    DOWN = pygame.K_DOWN
    LEFT = pygame.K_LEFT
    RIGHT = pygame.K_RIGHT
    QUIT = pygame.K_ESCAPE
    SPACE = pygame.K_SPACE

    ALL_KEYS = [
        UP,
        DOWN,
        LEFT,
        RIGHT,
        QUIT,
        SPACE,
    ]


KEY_DIRECTIONS = {
    Controls.UP: Vector2D(0, -1),
    Controls.DOWN: Vector2D(0, 1),
    Controls.LEFT: Vector2D(-1, 0),
    Controls.RIGHT: Vector2D(1, 0),
}

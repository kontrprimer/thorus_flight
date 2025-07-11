import pygame
from .framework import Vector


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
    Controls.UP: Vector([0, -1]),
    Controls.DOWN: Vector([0, 1]),
    Controls.LEFT: Vector([-1, 0]),
    Controls.RIGHT: Vector([1, 0]),
}

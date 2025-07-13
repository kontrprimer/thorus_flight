from .framework import Vector2D
from .units.player import Player
from .units.enemies import Enemy
from .controls import KEY_DIRECTIONS
from .colours import BLACK

import pygame


class Scene:
    def __init__(self, player: Player, screen_size: Vector2D):
        self.player = player
        self.screen_size = screen_size

    def update(self):
        raise NotImplementedError

    def draw(self, screen):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError

    @property
    def finished(self):
        raise NotImplementedError


class Stage01(Scene):
    def __init__(self, player: Player, screen_size: Vector2D):
        super().__init__(player, screen_size)
        self.enemies = [
            Enemy(Vector2D(-69, -69), target=player, screen_size=screen_size),
            Enemy(
                screen_size + Vector2D(69, 69), target=player, screen_size=screen_size
            ),
        ]

    def update(self):
        keys = pygame.key.get_pressed()
        self.accelerate_units(keys)
        self.update_units()

    def draw(self, screen):
        screen.fill(BLACK)
        for enemy in self.enemies:
            enemy.draw(screen)
        self.player.draw(screen)

    def update_units(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()
            enemy.try_attack()

    def accelerate_units(self, keys):
        acceleration = Vector2D(0, 0)
        for key, step in KEY_DIRECTIONS.items():
            if keys[key]:
                acceleration += step
        acceleration = acceleration.limit(1)
        self.player.accelerate(acceleration)
        for enemy in self.enemies:
            enemy.accelerate()

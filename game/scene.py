from .framework.vector2d import Vector2D
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

    def exit_scene(self):
        raise NotImplementedError

    @property
    def finished(self):
        raise NotImplementedError


class Battle(Scene):
    def __init__(self, player: Player, screen_size: Vector2D):
        super().__init__(player, screen_size)
        self.enemies = self.define_enemies()
        self.player.enemies = self.enemies

    def define_enemies(self) -> list[Enemy]:
        raise NotImplementedError

    def update(self):
        keys = pygame.key.get_pressed()
        self.accelerate_units(keys)
        self.update_units(keys)

    def draw(self, screen):
        screen.fill(BLACK)
        for enemy in self.enemies:
            enemy.draw(screen)
        self.player.draw(screen)

    def update_units(self, keys):
        self.player.update(keys)
        self.enemies = [enemy for enemy in self.enemies if enemy.exists]
        for enemy in self.enemies:
            enemy.update(keys)
            enemy.try_attack()

    def finished(self):
        return len(self.enemies) == 0

    def accelerate_units(self, keys):
        acceleration = Vector2D(0, 0)
        for key, step in KEY_DIRECTIONS.items():
            if keys[key]:
                acceleration += step
        acceleration = acceleration.limit(1)
        self.player.accelerate(acceleration)
        for enemy in self.enemies:
            enemy.accelerate()


class Battle01(Battle):
    def define_enemies(self):
        return [
            Enemy(Vector2D(-69, -69), target=self.player, screen_size=self.screen_size),
        ]

    def exit_scene(self):
        return Battle02(self.player, self.screen_size)


class Battle02(Battle):
    def define_enemies(self):
        return [
            Enemy(Vector2D(-69, -69), target=self.player, screen_size=self.screen_size),
            Enemy(
                self.screen_size + Vector2D(69, 69),
                target=self.player,
                screen_size=self.screen_size,
            ),
        ]

    def exit_scene(self):
        return self

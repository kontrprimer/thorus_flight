from .framework.vector2d import Vector2D
from .units.player import Player
from .units.enemies import Enemy
from .controls import KEY_DIRECTIONS, Controls
from .colours import BLACK, WHITE

import pygame


class Scene:
    def __init__(self, player: Player, screen_size: Vector2D):
        self.player = player
        self.screen_size = screen_size
        self._end_game = False

    def update(self):
        raise NotImplementedError

    def draw(self, screen):
        raise NotImplementedError

    def exit_scene(self):
        raise NotImplementedError

    @property
    def end_game(self):
        return self._end_game

    def finished(self):
        raise NotImplementedError


class Battle(Scene):
    def __init__(self, player: Player, screen_size: Vector2D):
        super().__init__(player, screen_size)
        self.enemies = self.define_enemies()
        self.player.enemies = self.enemies
        self.air_friction = 0.01

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
        self.accelerate_player(keys)
        for enemy in self.enemies:
            enemy.accelerate()
            self.slow_down_unit(enemy)

    def slow_down_unit(self, unit):
        unit.speed = unit.speed * (1 - self.air_friction / unit.aerodynamics)

    def accelerate_player(self, keys):
        acceleration = Vector2D(0, 0)
        for key, step in KEY_DIRECTIONS.items():
            if keys[key]:
                acceleration += step
        acceleration = acceleration.limit(1)
        self.player.accelerate(acceleration)
        self.slow_down_unit(self.player)


class Battle01(Battle):
    def define_enemies(self):
        size = 25
        return [
            Enemy(
                position=Vector2D(-size, -size),
                target=self.player,
                screen_size=self.screen_size,
                size=size,
            ),
        ]

    def exit_scene(self):
        return Battle02(self.player, self.screen_size)


class Battle02(Battle):
    def define_enemies(self):
        size = 25
        return [
            Enemy(
                position=Vector2D(-size, -size),
                target=self.player,
                screen_size=self.screen_size,
                size=size,
            ),
            Enemy(
                position=self.screen_size + Vector2D(size, size),
                target=self.player,
                screen_size=self.screen_size,
                size=size,
            ),
        ]

    def exit_scene(self):
        return WinScreen(self.player, self.screen_size)


class WinScreen(Scene):
    def __init__(self, player: Player, screen_size: Vector2D):
        super().__init__(player, screen_size)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[Controls.QUIT]:
            self._end_game = True

    def draw(self, screen):
        screen.fill(BLACK)
        font = pygame.font.Font(None, 60)
        text = font.render("You Win!", True, WHITE)
        text_rect = text.get_rect(center=list(self.screen_size * 0.5))
        screen.blit(text, text_rect)

    def finished(self):
        return False


class LoseScreen(Scene):
    def __init__(self, player: Player, screen_size: Vector2D):
        super().__init__(player, screen_size)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[Controls.QUIT]:
            self._end_game = True

    def draw(self, screen):
        screen.fill(BLACK)
        font = pygame.font.Font(None, 60)
        text = font.render("You Lose!", True, WHITE)
        text_rect = text.get_rect(center=list(self.screen_size * 0.5))
        screen.blit(text, text_rect)

    def finished(self):
        return False

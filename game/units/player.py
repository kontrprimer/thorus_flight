import time

import pygame.draw

from game.framework.vector2d import Vector2D
from game.framework.draw_image import draw_image
from .character import Character
from ..controls import Controls


class Player(Character):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.enemies: list[Character] = []
        self.weapons: list[Weapon] = [Weapon(self.pos)]

    def accelerate(self, direction: Vector2D):
        self.speed += direction * 0.1 / self.mass

    def draw_character(self, screen):
        draw_image(
            screen,
            image_path="data/ship_2_a.png",  # Replace with your SVG file path
            pos=self.pos,
            scale_k=self.size / 128 * 1.3,
            rotation_deg=self.speed.angle(degrees=True)
            + 90,  # Rotation angle in degrees
        )

    def draw(self, screen):
        for weapon in self.weapons:
            weapon.draw(screen)
        super().draw(screen)
        self.draw_hp_bar(screen)

    def update(self, keys):
        super().update(keys)
        for weapon in self.weapons:
            weapon.pos = self.pos
            if keys[weapon.key]:
                weapon.try_attack(self.enemies)

    def draw_hp_bar(self, screen):
        screen_size = list(self.screen_size)
        bar_width = screen_size[0] // 4  # HP bar takes up 1/4 of screen width
        bar_height = screen_size[1] // 30  # Thin bar relative to screen height
        margin = 20  # Padding from edges

        # Calculate position in bottom-left corner
        x = margin
        y = screen_size[1] - bar_height - margin

        # Calculate fill percentage
        fill_ratio = max(
            0.0, min(self.current_hp / self.max_hp, 1.0)
        )  # Clamp between 0 and 1
        fill_width = int(bar_width * fill_ratio)

        # Colors
        bg_color = (60, 60, 60)  # Dark gray background
        hp_color = (200, 50, 50)  # Red fill
        border_color = (255, 255, 255)  # White border

        # Draw background
        pygame.draw.rect(screen, bg_color, (x, y, bar_width, bar_height))

        # Draw filled portion
        pygame.draw.rect(screen, hp_color, (x, y, fill_width, bar_height))

        # Draw border
        pygame.draw.rect(screen, border_color, (x, y, bar_width, bar_height), 2)


class Weapon:
    def __init__(self, pos: Vector2D):
        self.damage: float = 5000
        self.range: float = 200
        self.push_power: float = 15
        self.pos: Vector2D = pos
        self.cooldown: float = 1
        self.last_attack_time: float = 0
        self.key = Controls.SPACE

    def try_attack(self, targets: list[Character]):
        current_time = time.time()
        if current_time - self.last_attack_time < self.cooldown:
            return
        self.last_attack_time = current_time
        for target in targets:
            to_target = target.pos - self.pos
            distance_to_target = to_target.length
            if distance_to_target <= self.range:
                power = 1 - (distance_to_target / self.range)
                target.take_damage(self.damage * power)
                target.speed += to_target.set_length(self.push_power * power)

    def draw(self, screen):
        effect_time = 0.05
        current_time = time.time()
        time_since_attack = current_time - self.last_attack_time
        if time_since_attack < effect_time:
            effect_intensity = time_since_attack / effect_time
            pygame.draw.circle(
                screen,
                (180 + 75 * effect_intensity, 100 + 155 * effect_intensity, 255),
                list(self.pos),
                self.range * effect_intensity,
            )

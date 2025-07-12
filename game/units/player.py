import pygame.draw
from game.framework import Vector2D, draw_svg
from game.units.trail import UnitTrail


class Player:
    def __init__(self, position: Vector2D, screen_size: Vector2D):
        self.pos = position
        self.speed = Vector2D(0.0, 0.0)
        self.max_speed = 50
        self.max_hp = 100.0
        self.current_hp = 100.0
        self.screen_size = screen_size
        self.margin = Vector2D(70, 70)
        self.space_size = screen_size + self.margin * 2
        self.__trails: list[UnitTrail] = []

    def update(self):
        for trail in self.__trails:
            trail.update()
        self.__trails = [trail for trail in self.__trails if trail.exists]
        self.__trails.append(UnitTrail(self.pos, size=12, decay_speed=0.2))
        self.pos = (self.pos + self.margin + self.speed) % self.space_size - self.margin

    def get_damage(self, damage: float):
        self.current_hp = max(self.current_hp - damage, 0)

    def accelerate(self, direction: Vector2D):
        self.speed += direction * 0.08
        self.speed = self.speed.limit(self.max_speed)

    def draw(self, screen):
        for trail in self.__trails:
            trail.draw(screen)
        draw_svg(
            screen,
            svg_path="data/ship_2_a.svg",  # Replace with your SVG file path
            pos=self.pos,
            scale_k=0.15,
            rotation_deg=self.speed.angle,  # Rotation angle in degrees
        )
        self.draw_hp_bar(screen)

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

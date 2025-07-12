import pygame.draw
import time
from game.framework import Vector2D, draw_svg


class Player:
    def __init__(self, position: Vector2D, screen_size: Vector2D):
        self.pos = position
        self.speed = Vector2D(0.1, 5.1)
        self.max_speed = 50
        self.max_hp = 100.0
        self.current_hp = 100.0
        self.screen_size = screen_size
        self.__trails: list[UnitTrail] = []

    def update(self):
        for trail in self.__trails:
            trail.update()
        self.__trails = [trail for trail in self.__trails if trail.exists]
        self.__trails.append(UnitTrail(self.pos, size=12, decay_speed=0.2))
        self.pos = (self.pos + self.speed) % self.screen_size

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


class Enemy:
    def __init__(self, position: Vector2D, target: Player):
        self.pos = position
        self.target = target
        self.speed = Vector2D(0.1, 0.1)
        self.max_speed = 6
        self.__trails: list[UnitTrail] = []
        self.__last_attack_time = 0.0

    def update(self, clip: Vector2D):
        for trail in self.__trails:
            trail.update()
        self.__trails = [trail for trail in self.__trails if trail.exists]
        self.__trails.append(UnitTrail(self.pos, size=12, decay_speed=0.2))
        self.pos = (self.pos + self.speed) % clip

    def accelerate(self):
        direction = self.target.pos - self.pos
        self.speed += direction.set_length(0.05)
        self.speed = self.speed.limit(self.max_speed)

    def try_attack(self):
        if time.time() - self.__last_attack_time < 1:
            return
        from_target_vector = self.pos - self.target.pos
        if from_target_vector.length < 50:
            self.target.get_damage(10)
            self.speed = from_target_vector.set_length(self.max_speed)
            self.__last_attack_time = time.time()

    def draw(self, screen):
        for trail in self.__trails:
            trail.draw(screen)
        draw_svg(
            screen,
            svg_path="data/ship_1_a.svg",  # Replace with your SVG file path
            pos=self.pos,
            scale_k=0.15,
            rotation_deg=self.speed.angle,  # Rotation angle in degrees
        )


class UnitTrail:
    def __init__(self, pos, size, decay_speed):
        self.pos = pos
        self.size = size
        self.original_size = size
        self.decay_speed = decay_speed

    def update(self):
        self.size = max(0, self.size - self.decay_speed)

    def draw(self, screen):
        intensity = self.size / self.original_size
        pygame.draw.circle(
            screen,
            (180 + 75 * intensity, 100 + 155 * intensity, 255),
            list(self.pos),
            self.size,
        )

    @property
    def exists(self):
        return self.size > 0

from game.framework import Vector, draw_svg


class Player:
    def __init__(self, position: Vector):
        self.pos = position
        self.speed = Vector([0.001, 0.5])
        self.max_speed = 1

    def move(self, clip: Vector):
        self.pos = (self.pos + self.speed) % clip

    def accelerate(self, direction: Vector):
        self.speed += direction * 0.0008
        self.speed = self.speed.limit(self.max_speed)

    def draw(self, screen):
        draw_svg(
            screen,
            svg_path="ship_2.svg",  # Replace with your SVG file path
            pos=self.pos,
            scale_k=0.15,
            rotation_deg=self.speed.angle,  # Rotation angle in degrees
        )

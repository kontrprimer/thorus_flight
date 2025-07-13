from game.framework.vector2d import Vector2D


class Unit:
    def __init__(self, position: Vector2D, screen_size: Vector2D):
        self.pos = position
        self.speed = Vector2D(0.0, 0.0)
        self.screen_size = screen_size
        self.margin = Vector2D(70, 70)
        self.space_size = screen_size + self.margin * 2

    def update(self, keys):
        self.pos = (self.pos + self.margin + self.speed) % self.space_size - self.margin

    def draw(self, screen):
        raise NotImplementedError

    @property
    def exists(self):
        raise NotImplementedError

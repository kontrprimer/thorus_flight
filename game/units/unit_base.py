from game.framework.vector2d import Vector2D


class Unit:
    def __init__(
        self,
        position: Vector2D,
        screen_size: Vector2D,
        mass: float = 1,
        size: float = 10,
    ):
        self.pos = position
        self.speed = Vector2D(0.0, 0.0)
        self.screen_size = screen_size

        self.size = size
        self.screen_margin_size = Vector2D(size + 1, size + 1)
        self.space_size = screen_size + self.screen_margin_size * 2

        self.mass = mass

    def update(self, keys):
        self.pos = (
            self.pos + self.screen_margin_size + self.speed
        ) % self.space_size - self.screen_margin_size

    def draw(self, screen):
        raise NotImplementedError

    @property
    def exists(self):
        raise NotImplementedError

from game.framework.vector2d import Vector2D


class Unit:
    def __init__(
        self,
        position: Vector2D,
        screen_size: Vector2D,
        direction: float = 0,
        mass: float = 1,
        size: float = 10,
        aerodynamics: float = 1,
    ):
        self.pos = position
        self.speed = Vector2D(0.0, 0.0)
        self.direction = direction
        self.turn_speed: float = 0
        self.turn_acceleration: float = 1
        self.screen_size = screen_size

        self.size = size
        self.screen_margin_size = Vector2D(size + 1, size + 1)
        self.space_size = screen_size + self.screen_margin_size * 2

        self.mass = mass
        self.aerodynamics = aerodynamics

    def update(self, keys):
        self.pos = (
            self.pos + self.screen_margin_size + self.speed
        ) % self.space_size - self.screen_margin_size

    def draw(self, screen):
        raise NotImplementedError

    @property
    def exists(self):
        raise NotImplementedError

    def take_damage(self, damage: float):
        raise NotImplementedError

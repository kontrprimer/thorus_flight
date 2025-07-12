import io
from functools import cache

import cairosvg
import pygame
import math


class Vector2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __eq__(self, other: "Vector2D"):
        return self.__x == other.__x and self.__y == other.__y

    def __mul__(self, num: float):
        return Vector2D(self.__x * num, self.__y * num)

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.__x - other.__x, self.__y - other.__y)

    def __mod__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.__x % other.__x, self.__y % other.__y)

    def __truediv__(self, num: float) -> "Vector2D":
        return Vector2D(self.__x * num, self.__y * num)

    def __iter__(self):
        return iter([self.__x, self.__y])

    @property
    def angle(self) -> float:
        return math.degrees(math.atan2(self.__y, self.__x)) + 90

    @property
    def length(self) -> float:
        return (self.__x * self.__x + self.__y * self.__y) ** 0.5

    def limit(self, limit: float) -> "Vector2D":
        length = self.length
        if length > limit:
            ratio = limit / length
            return self * ratio
        return self

    def set_length(self, length: float) -> "Vector2D":
        if self == Vector2D(0, 0):
            return Vector2D(length, 0)
        ratio = length / self.length
        return self * ratio


@cache
def load_svg_as_surface(svg_path, scale=1.0):
    # Convert SVG to PNG in memory
    png_data = cairosvg.svg2png(
        url=svg_path, output_width=None, output_height=None, scale=scale
    )
    return pygame.image.load(io.BytesIO(png_data)).convert_alpha()


def draw_svg(screen, svg_path, pos: Vector2D, scale_k, rotation_deg):
    svg_surf = load_svg_as_surface(svg_path, scale=scale_k)

    # Smooth anti-aliased rotation
    rotated_surf = pygame.transform.rotozoom(svg_surf, -rotation_deg, 1.0)

    rect = rotated_surf.get_rect(center=list(pos))
    screen.blit(rotated_surf, rect)

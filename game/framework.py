import io
from functools import cache

import cairosvg
import pygame
import math


class Vector:
    def __init__(self, coordinates):
        self.__coordinates = list(coordinates)

    def __len__(self):
        return len(self.__coordinates)

    def __eq__(self, other: "Vector"):
        return self.__coordinates == other.__coordinates

    def __mul__(self, num: float):
        return Vector([x * num for x in self.__coordinates])

    def __add__(self, other: "Vector") -> "Vector":
        return Vector([i + j for i, j in zip(self.__coordinates, other.__coordinates)])

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector([i - j for i, j in zip(self.__coordinates, other.__coordinates)])

    def __mod__(self, other: "Vector") -> "Vector":
        return Vector([i % j for i, j in zip(self.__coordinates, other.__coordinates)])

    def __truediv__(self, other: float) -> "Vector":
        return Vector([i / other for i in self.__coordinates])

    def __iter__(self):
        return iter(self.__coordinates)

    @property
    def angle(self) -> float:
        return (
            math.degrees(math.atan2(self.__coordinates[1], self.__coordinates[0])) + 90
        )

    @property
    def length(self) -> float:
        return sum(i**2 for i in self.__coordinates) ** 0.5

    def limit(self, limit: float) -> "Vector":
        length = self.length
        if length > limit:
            ratio = limit / length
            return self * ratio
        return self


@cache
def load_svg_as_surface(svg_path, scale=1.0):
    # Convert SVG to PNG in memory
    png_data = cairosvg.svg2png(
        url=svg_path, output_width=None, output_height=None, scale=scale
    )
    return pygame.image.load(io.BytesIO(png_data)).convert_alpha()


def draw_svg(screen, svg_path, pos: Vector, scale_k, rotation_deg):
    # Load and scale SVG
    svg_surf = load_svg_as_surface(svg_path, scale=scale_k)

    # Rotate the surface
    rotated_surf = pygame.transform.rotate(
        svg_surf, -rotation_deg
    )  # Negative to rotate clockwise

    # Get new rect and center it at (x, y)
    rect = rotated_surf.get_rect(center=list(pos))

    # Draw to the screen
    screen.blit(rotated_surf, rect)

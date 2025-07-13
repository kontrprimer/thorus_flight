from functools import cache
import pygame


@cache
def load_png_as_surface(png_path):
    return pygame.image.load(png_path).convert_alpha()

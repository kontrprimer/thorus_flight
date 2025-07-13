import pygame

from game.framework.load_svg import load_svg_as_surface
from game.framework.load_png import load_png_as_surface
from game.framework.vector2d import Vector2D

import os


def draw_image(screen, image_path, pos: Vector2D, scale_k, rotation_deg):
    ext = os.path.splitext(image_path)[1].lower()

    if ext == ".svg":
        # SVG handles scaling during loading
        surf = load_svg_as_surface(image_path, scale=scale_k)
        transformed_surf = pygame.transform.rotozoom(surf, -rotation_deg, 1.0)
    else:
        # PNG handles scaling during transform
        surf = load_png_as_surface(image_path)
        transformed_surf = pygame.transform.rotozoom(surf, -rotation_deg, scale_k)

    rect = transformed_surf.get_rect(center=list(pos))
    screen.blit(transformed_surf, rect)

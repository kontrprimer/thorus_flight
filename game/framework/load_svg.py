import io
from functools import cache

import pygame


@cache
def load_svg_as_surface(svg_path, scale=1.0):
    import cairosvg

    # Convert SVG to PNG in memory
    png_data = cairosvg.svg2png(
        url=svg_path, output_width=None, output_height=None, scale=scale
    )
    return pygame.image.load(io.BytesIO(png_data)).convert_alpha()

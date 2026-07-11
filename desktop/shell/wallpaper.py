"""
Gorgon OS (VOS)

Wallpaper Layer (Figma Style)
"""

from __future__ import annotations

import pygame


class Wallpaper:

    def __init__(self):

        self.image = None

    def set_image(self, image):

        self.image = image

    def draw(self, renderer, width: int, height: int):

        surface = renderer.surface

        # If no image, use gradient fallback (matches Figma style better than flat color)

        if self.image is None:

            for y in range(height):

                ratio = y / height

                r = int(18 + ratio * 10)
                g = int(22 + ratio * 18)
                b = int(35 + ratio * 40)

                pygame.draw.line(
                    surface,
                    (r, g, b),
                    (0, y),
                    (width, y),
                )

            return

        renderer.draw_image(
            self.image,
            pygame.Rect(0, 0, width, height),
            keep_aspect=False,
        )
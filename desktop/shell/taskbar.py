"""
Gorgon OS (VOS)

Taskbar
"""

from __future__ import annotations

import pygame


class Taskbar:

    HEIGHT = 64

    def draw(self, renderer):

        surface = renderer.surface

        width = surface.get_width()
        height = surface.get_height()

        # Background

        pygame.draw.rect(
            surface,
            (34, 37, 45),
            (
                18,
                height - 82,
                width - 36,
                64,
            ),
            border_radius=22,
        )

        # Start Button

        pygame.draw.circle(
            surface,
            (63, 130, 255),
            (
                58,
                height - 50,
            ),
            18,
        )

        # App Icons

        x = 115

        for _ in range(5):

            pygame.draw.circle(
                surface,
                (200, 200, 200),
                (
                    x,
                    height - 50,
                ),
                14,
            )

            x += 46

        # Clock

        font = pygame.font.SysFont(
            "arial",
            20,
        )

        renderer.draw_text(
            "12:45",
            font,
            (255, 255, 255),
            pygame.Vector2(
                width - 80,
                height - 60,
            ),
        )
"""
Gorgon OS (VOS)

Wallpaper
"""

from __future__ import annotations

import pygame

from resources.asset_manager import AssetManager


class Wallpaper:

    def __init__(self) -> None:

        self.image = None

        try:

            self.image = AssetManager().load_image(
                "wallpapers/default.png"
            )

        except Exception:

            self.image = None

    def draw(
        self,
        renderer,
        width: int,
        height: int,
    ) -> None:

        if self.image is None:
            return

        renderer.draw_image(
            self.image,
            pygame.Rect(
                0,
                0,
                width,
                height,
            ),
            keep_aspect=False,
        )
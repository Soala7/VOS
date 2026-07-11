"""
Gorgon OS (VOS)

SVG Icon Manager
"""

from __future__ import annotations

from pathlib import Path

import pygame
import cairosvg
from io import BytesIO

class IconManager:

    _cache: dict[tuple[str, int], pygame.Surface] = {}

    ROOT = Path("assets/icons")

    @classmethod
    def get(
        cls,
        icon: str,
        size: int = 60,
    ) -> pygame.Surface | None:

        key = (icon, size)

        if key in cls._cache:
            return cls._cache[key]

        path = cls.ROOT / f"{icon}.svg"

        if not path.exists():

            print(f"[IconManager] Missing icon: {path}")

            return None

        png_bytes = cairosvg.svg2png(
            url=str(path),
            output_width=size,
            output_height=size,
        )

        try:
            surface = pygame.image.load(
                BytesIO(png_bytes),
                "icon.png",
            ).convert_alpha()

        except Exception as e:

            print(f"[IconManager] Failed to load {icon}: {e}")

            return None

        cls._cache[key] = surface
        print(f"[IconManager] Loaded {icon}")

        return surface

    @classmethod
    def clear_cache(cls):

        cls._cache.clear()
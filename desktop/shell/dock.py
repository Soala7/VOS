"""
Gorgon OS (VOS)

Dock
"""

from __future__ import annotations

import pygame

from desktop.ui.widgets.widget import Widget
from desktop.assests.icon_manager import IconManager


class Dock(Widget):

    ICON_SIZE = 60
    SLOT_SIZE = 70
    MAX_ICONS = 7
    SPACING = 18
    BOTTOM_MARGIN = 35

    def __init__(self) -> None:

        super().__init__("Dock")

        self.icons = [

            IconManager.get("launcher/browser", self.ICON_SIZE),
            IconManager.get("launcher/explorer", self.ICON_SIZE),
            IconManager.get("launcher/music", self.ICON_SIZE),
            IconManager.get("launcher/note", self.ICON_SIZE),
            IconManager.get("launcher/settings", self.ICON_SIZE),
            IconManager.get("launcher/terminal", self.ICON_SIZE),
            IconManager.get("launcher/store", self.ICON_SIZE),

        ]

    # --------------------------------------------------

    def update(self, dt: float) -> None:

        pass

    # --------------------------------------------------

    def draw(self, renderer) -> None:

        surface = renderer.surface

        width = surface.get_width()
        height = surface.get_height()

        total_width = (
            self.MAX_ICONS * self.SLOT_SIZE
            + (self.MAX_ICONS - 1) * self.SPACING
        )

        start_x = (width - total_width) // 2

        y = (
            height
            - self.BOTTOM_MARGIN
            - self.SLOT_SIZE
        )

        for i in range(self.MAX_ICONS):

            x = start_x + i * (
                self.SLOT_SIZE + self.SPACING
            )

            # Shadow

            shadow = pygame.Surface(
                (self.SLOT_SIZE, self.SLOT_SIZE),
                pygame.SRCALPHA,
            )

            pygame.draw.circle(
                shadow,
                (0, 0, 0, 55),
                (
                    self.SLOT_SIZE // 2,
                    self.SLOT_SIZE // 2,
                ),
                self.SLOT_SIZE // 2,
            )

            surface.blit(shadow, (x, y))

            # Background

            pygame.draw.circle(
                surface,
                (52, 52, 58),
                (
                    x + self.SLOT_SIZE // 2,
                    y + self.SLOT_SIZE // 2,
                ),
                self.SLOT_SIZE // 2,
            )

            pygame.draw.circle(
                surface,
                (95, 95, 105),
                (
                    x + self.SLOT_SIZE // 2,
                    y + self.SLOT_SIZE // 2,
                ),
                self.SLOT_SIZE // 2,
                1,
            )

            # Icon

            icon = self.icons[i]

            if icon is not None:

                surface.blit(
                    icon,
                    (
                        x + (self.SLOT_SIZE - icon.get_width()) // 2,
                        y + (self.SLOT_SIZE - icon.get_height()) // 2,
                    ),
                )
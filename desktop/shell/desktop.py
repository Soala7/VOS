"""
Gorgon OS (VOS)

Desktop
"""

from __future__ import annotations

from desktop import renderer
from desktop.ui.widgets.panel import Panel
from desktop.shell.wallpaper import Wallpaper
from desktop.ui.window.window_manager import WindowManager
from desktop.shell.compositor import Compositor
from desktop.shell.start_menu import StartMenu
from desktop.shell.status_bar import StatusBar

import pygame

class Desktop(Panel):
    """
    Root desktop container.
    """

    def __init__(self) -> None:

        super().__init__("Desktop")

        self.status_bar = StatusBar()

        self.wallpaper = Wallpaper()
        wallpaper = pygame.image.load(
                "assets/wallpapers/default.png"
            ).convert()

        self.wallpaper.set_image(wallpaper)

        self.window_manager = WindowManager()

        self.compositor = Compositor(self)

        self.start_menu = StartMenu()

        self.launcher = None

    def set_wallpaper(self, image) -> None:

        self.wallpaper.set_image(image)

    def add_window(self, window) -> None:

        self.window_manager.add_window(window)

    def remove_window(self, window) -> None:

        self.window_manager.remove_window(window)

    def update(self, dt: float) -> None:

        super().update(dt)

        self.window_manager.update(dt)

    def draw(self, renderer) -> None:

        # Wallpaper
        self.wallpaper.draw(
            renderer,
            renderer.surface.get_width(),
            renderer.surface.get_height(),
        )

        # Draw all children (Dock, Launcher, Desktop Icons, etc.)
        super().draw(renderer)

        # Windows
        self.window_manager.draw(renderer)

        # Status Bar
        self.status_bar.draw(renderer)

    def handle_event(self, event) -> None:

        super().handle_event(event)

        self.window_manager.handle_event(event)
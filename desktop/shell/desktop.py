"""
Gorgon OS (VOS)

Desktop
"""

from __future__ import annotations

from desktop.ui.widgets.panel import Panel
from desktop.shell.wallpaper import Wallpaper
from desktop.ui.window.window_manager import WindowManager
from desktop.shell.taskbar import Taskbar


class Desktop(Panel):
    """
    Root desktop container.
    """

    def __init__(self) -> None:

        super().__init__("Desktop")

        self.wallpaper = Wallpaper()

        self.window_manager = WindowManager()

        self.taskbar = Taskbar()

    def set_wallpaper(self, image) -> None:

        self.wallpaper.set_image(image)

    def add_window(self, window) -> None:

        self.window_manager.add_window(window)

    def remove_window(self, window) -> None:

        self.window_manager.remove_window(window)

    def update(self, dt: float) -> None:

        super().update(dt)

        self.window_manager.update(dt)

    def draw(self, renderer):
        renderer.clear((24, 31, 46))

        self.taskbar.draw(renderer)
    def handle_event(self, event) -> None:

        super().handle_event(event)

        self.window_manager.handle_event(event)
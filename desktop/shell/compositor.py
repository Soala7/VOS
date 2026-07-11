"""
Gorgon OS (VOS)

Desktop Compositor
"""

from __future__ import annotations


class Compositor:
    """
    Responsible for drawing the desktop in the correct order.
    """

    def __init__(self, desktop):

        self.desktop = desktop

    # --------------------------------------------------
    # Draw
    # --------------------------------------------------

    def draw(self, renderer):

        surface = renderer.surface

        width = surface.get_width()
        height = surface.get_height()

        # ------------------------------------------
        # Wallpaper
        # ------------------------------------------

        self.desktop.wallpaper.draw(
            renderer,
            width,
            height,
        )

        # ------------------------------------------
        # Desktop Widgets (future)
        # ------------------------------------------

        # self.desktop.widgets.draw(renderer)

        # ------------------------------------------
        # Desktop Icons
        # ------------------------------------------

        if hasattr(self.desktop, "desktop_icons"):
            self.desktop.desktop_icons.draw(renderer)

        # ------------------------------------------
        # Windows
        # ------------------------------------------

        self.desktop.window_manager.draw(renderer)

        # ------------------------------------------
        # Dock 
        # ------------------------------------------

        if hasattr(self.desktop, "dock"):
            self.desktop.dock.draw(renderer)

        # ------------------------------------------
        # Start Menu
        # ------------------------------------------

        if (
            hasattr(self.desktop, "start_menu")
            and self.desktop.start_menu.visible
        ):
            self.desktop.start_menu.draw(renderer)

        # ------------------------------------------
        # Notifications
        # ------------------------------------------

        if (
            hasattr(self.desktop, "notification_center")
            and self.desktop.notification_center.visible
        ):
            self.desktop.notification_center.draw(renderer)
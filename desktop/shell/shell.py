"""
Gorgon OS (VOS)

Shell
"""

from __future__ import annotations

from desktop.shell.desktop import Desktop
from desktop.shell.taskbar import Taskbar
from desktop.shell.start_menu import StartMenu
from desktop.shell.notification_center import NotificationCenter
from desktop.shell.desktop_icons import DesktopIcons


class Shell:
    """
    Main desktop shell.
    """

    def __init__(self) -> None:

        self.desktop = Desktop()

        self.taskbar = Taskbar()

        self.start_menu = StartMenu()

        self.notification_center = NotificationCenter()

        self.desktop_icons = DesktopIcons()

        self.desktop.add_child(self.desktop_icons)

        self.desktop.add_child(self.start_menu)

        self.desktop.add_child(self.notification_center)

    # --------------------------------------------------
    # Update
    # --------------------------------------------------

    def update(self, dt: float) -> None:

        self.desktop.update(dt)

    # --------------------------------------------------
    # Draw
    # --------------------------------------------------

    def draw(self, renderer) -> None:

        self.desktop.draw(renderer)

    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def handle_event(self, event) -> None:

        self.desktop.handle_event(event)
"""
Gorgon OS (VOS)

Shell
"""

from __future__ import annotations

from desktop.renderer import renderer
from desktop.shell.desktop import Desktop
from desktop.shell.dock import Dock
from desktop.shell.launcher import Launcher
from desktop.shell.notification_center import NotificationCenter
from desktop.shell.desktop_icons import DesktopIcons


class Shell:
    """
    Main desktop shell.
    """

    def __init__(self) -> None:

        self.desktop = Desktop()

        self.dock = Dock()

        self.launcher = Launcher()

        self.notification_center = NotificationCenter()

        self.desktop_icons = DesktopIcons()

        self.desktop_icons.layer = 10
        self.dock.layer = 40
        self.launcher.layer = 50
        self.notification_center.layer = 60

        self.desktop.add_child(self.desktop_icons)
        self.desktop.add_child(self.dock)
        self.desktop.add_child(self.launcher)
        self.desktop.add_child(self.notification_center)

        # Give the dock access to the launcher
        self.dock.launcher = self.launcher
        self.desktop.launcher = self.launcher

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
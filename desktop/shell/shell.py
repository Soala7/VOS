"""
Gorgon OS (VOS)

Shell
"""

from __future__ import annotations

from desktop.shell.desktop import Desktop
from desktop.shell.dock import Dock
from desktop.shell.start_menu import StartMenu
from desktop.shell.notification_center import NotificationCenter


class Shell:
    """
    Main desktop shell.
    """

    def __init__(self) -> None:

        self.desktop = Desktop()

        self.dock = Dock()

        self.start_menu = StartMenu()

        self.notification_center = NotificationCenter()

        # Order matters (draw order)

        self.desktop.add_child(self.dock)

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
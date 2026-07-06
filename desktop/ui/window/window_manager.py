"""
Gorgon OS (VOS)

Window Manager
"""

from __future__ import annotations

from desktop.ui.window.window import Window


class WindowManager:
    """
    Manages all desktop windows.
    """

    def __init__(self) -> None:

        self.windows: list[Window] = []

        self.active_window: Window | None = None

    # --------------------------------------------------
    # Window Management
    # --------------------------------------------------

    def add_window(self, window: Window) -> None:

        if window not in self.windows:

            self.windows.append(window)

            self.focus_window(window)

    def remove_window(self, window: Window) -> None:

        if window in self.windows:

            self.windows.remove(window)

            if self.active_window is window:
                self.active_window = None

    def close_window(self, window: Window) -> None:

        window.close()

        self.remove_window(window)

    # --------------------------------------------------
    # Focus
    # --------------------------------------------------

    def focus_window(self, window: Window) -> None:

        if window not in self.windows:
            return

        if self.active_window is not None:

            self.active_window.deactivate()

        self.active_window = window

        window.activate()

        self.windows.remove(window)

        self.windows.append(window)

    # --------------------------------------------------
    # Update
    # --------------------------------------------------

    def update(self, dt: float) -> None:

        closed = []

        for window in self.windows:

            window.update(dt)

            if window.closed:

                closed.append(window)

        for window in closed:

            self.remove_window(window)

    # --------------------------------------------------
    # Draw
    # --------------------------------------------------

    def draw(self, renderer) -> None:

        for window in self.windows:

            if not window.minimized:

                window.draw(renderer)

    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def handle_event(self, event) -> None:

        for window in reversed(self.windows):

            window.handle_event(event)

            if getattr(event, "handled", False):

                break
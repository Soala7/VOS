"""
Gorgon OS (VOS)

Window widget.
"""

from __future__ import annotations

from desktop.ui.widgets.panel import Panel


class Window(Panel):
    """
    Base window class.
    """

    def __init__(
        self,
        title: str = "Window",
        width: int = 800,
        height: int = 600,
        name: str = "Window",
    ) -> None:

        super().__init__(name)

        self.title = title

        self.transform.resize(width, height)

        self.minimized = False
        self.maximized = False
        self.closed = False

        self.draggable = True
        self.resizable = True

        self.active = False

    def minimize(self) -> None:

        self.minimized = True
        self.maximized = False

    def maximize(self) -> None:

        self.maximized = True
        self.minimized = False

    def restore(self) -> None:

        self.minimized = False
        self.maximized = False

    def close(self) -> None:

        self.closed = True
        self.destroy()

    def activate(self) -> None:

        self.active = True

    def deactivate(self) -> None:

        self.active = False
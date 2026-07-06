"""
Gorgon OS (VOS)

Desktop Icons
"""

from __future__ import annotations

from desktop.ui.widgets.panel import Panel
from desktop.ui.layout.vertical_layout import VerticalLayout


class DesktopIcons(Panel):
    """
    Container for desktop icons.
    """

    def __init__(self) -> None:

        super().__init__("DesktopIcons")

        self.layout = VerticalLayout(
            spacing=12,
            margin=12,
        )

    def add_icon(self, icon) -> None:

        self.add_child(icon)

        self.layout.apply(self)

    def remove_icon(self, icon) -> None:

        self.remove_child(icon)

        self.layout.apply(self)

    def clear_icons(self) -> None:

        self.clear_children()
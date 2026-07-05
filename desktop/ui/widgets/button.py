from desktop.ui.core.component import Component
from desktop.ui.core.event import MouseEvent, EventType


class Button(Component):
    def __init__(self, x, y, width, height, text="Button"):
        super().__init__(x, y, width, height)
        self.text = text
        self.clicked = False

    def on_event(self, event) -> bool:
        if isinstance(event, MouseEvent):
            if event.event_type == EventType.MOUSE_PRESS:
                self.clicked = True
                print(f"[BUTTON CLICKED] {self.text}")
                return True  # event consumed

        return False
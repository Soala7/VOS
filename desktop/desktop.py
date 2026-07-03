from core.logger import Logger
from desktop.window_manager import WindowManager


class Window:
    """
    Logical representation of a window in VOS Desktop.
    (No rendering yet — just structure)
    """

    def __init__(self, window_id, title, app_name):
        self.window_manager = WindowManager()
        self.window_id = window_id
        self.title = title
        self.app_name = app_name

        self.state = "OPEN"  # OPEN | MINIMIZED | CLOSED
        self.position = (100, 100)
        self.size = (800, 600)


class Desktop:
    """
    Core Desktop Environment (logical layer).
    Handles windows and UI state before rendering system is added.
    """

    def __init__(self, event_bus, app_manager):
        self.logger = Logger("Desktop")

        self.event_bus = event_bus
        self.app_manager = app_manager

        self.windows = {}
        self.next_window_id = 1

        self.running = False

    # ----------------------------
    # START DESKTOP
    # ----------------------------
    def start(self):
        self.logger.info("Desktop starting...")

        self.running = True

        # Listen to system events
        self._register_events()

        self.logger.info("Desktop ready.")

    # ----------------------------
    # EVENT SYSTEM
    # ----------------------------
    def _register_events(self):
        self.event_bus.subscribe("app:launched", self._on_app_launched)
        self.event_bus.subscribe("app:closed", self._on_app_closed)

    # ----------------------------
    # APP → WINDOW CREATION
    # ----------------------------
    def _on_app_launched(self, data):
        self.window_manager.create_window(
        title=data["name"].capitalize(),
        app_name=data["name"]
    )

    # ----------------------------
    # APP CLOSED → WINDOW REMOVAL
    # ----------------------------
    def _on_app_closed(self, data):
        pid = data["pid"]
        app = self.app_manager.running_apps.get(pid)
        if not app:
            return
        for window in self.window_manager.get_windows():
            if window.app_name == app.name:
                self.window_manager.close_window(window.id)
                break

    # ----------------------------
    # WINDOW MANAGEMENT
    # ----------------------------
    def list_windows(self):
        return list(self.windows.values())

    def get_window(self, window_id):
        return self.windows.get(window_id)
        
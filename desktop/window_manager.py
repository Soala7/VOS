from core.logger import Logger


class Window:
    """
    Represents a desktop window.
    """

    def __init__(self, window_id, title, app_name):
        self.id = window_id
        self.title = title
        self.app_name = app_name

        self.state = "NORMAL"

        self.position = (100, 100)
        self.size = (900, 600)

        self.visible = True
        self.focused = False

        # Higher value = drawn on top
        self.z_index = 0


class WindowManager:

    def __init__(self):
        self.logger = Logger("WindowManager")

        self.windows = {}
        self.active_window = None

        self.next_window_id = 1

    # -------------------------
    # CREATE
    # -------------------------

    def create_window(self, title, app_name):

        window = Window(
            self.next_window_id,
            title,
            app_name
        )

        window.z_index = self.next_window_id

        self.windows[self.next_window_id] = window

        self.next_window_id += 1

        self.focus_window(window.id)

        self.logger.info(
            f"Window created ({window.id}) : {title}"
        )

        return window

    # -------------------------
    # CLOSE
    # -------------------------

    def close_window(self, window_id):

        if window_id not in self.windows:
            return False

        self.logger.info(
            f"Closing window {window_id}"
        )

        del self.windows[window_id]

        if self.active_window == window_id:
            self.active_window = None

        return True

    # -------------------------
    # FOCUS
    # -------------------------

    def focus_window(self, window_id):

        if window_id not in self.windows:
            return

        for window in self.windows.values():
            window.focused = False

        window = self.windows[window_id]

        window.focused = True

        self.active_window = window_id

        highest = max(
            [w.z_index for w in self.windows.values()],
            default=0
        )

        window.z_index = highest + 1

        self.logger.info(
            f"Focused window {window.title}"
        )

    # -------------------------
    # MINIMIZE
    # -------------------------

    def minimize_window(self, window_id):

        if window_id not in self.windows:
            return

        self.windows[window_id].state = "MINIMIZED"

    # -------------------------
    # MAXIMIZE
    # -------------------------

    def maximize_window(self, window_id):

        if window_id not in self.windows:
            return

        self.windows[window_id].state = "MAXIMIZED"

    # -------------------------
    # RESTORE
    # -------------------------

    def restore_window(self, window_id):

        if window_id not in self.windows:
            return

        self.windows[window_id].state = "NORMAL"

    # -------------------------
    # MOVE
    # -------------------------

    def move_window(
        self,
        window_id,
        x,
        y
    ):

        if window_id not in self.windows:
            return

        self.windows[window_id].position = (x, y)

    # -------------------------
    # RESIZE
    # -------------------------

    def resize_window(
        self,
        window_id,
        width,
        height
    ):

        if window_id not in self.windows:
            return

        self.windows[window_id].size = (
            width,
            height
        )

    # -------------------------
    # GETTERS
    # -------------------------

    def get_window(self, window_id):

        return self.windows.get(window_id)

    def get_windows(self):

        return list(self.windows.values())
class FileSystem:
    def __init__(self, event_bus=None):
        self.files = {}
        self.event_bus = event_bus

    def create_file(self, path, content=""):
        self.files[path] = content

        if self.event_bus:
            self.event_bus.emit("file_created", {"path": path})

    def delete_file(self, path):
        if path in self.files:
            del self.files[path]

            if self.event_bus:
                self.event_bus.emit("file_deleted", {"path": path})

    def read_file(self, path):
        return self.files.get(path)
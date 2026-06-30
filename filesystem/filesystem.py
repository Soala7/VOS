class FileSystem:
    def __init__(self):
        self.files = {}

    def create_file(self, path, content=""):
        self.files[path] = content

    def read_file(self, path):
        return self.files.get(path)

    def delete_file(self, path):
        if path in self.files:
            del self.files[path]
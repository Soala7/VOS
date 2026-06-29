class Kernel:
    def __init__(self):
        self.file_manager = None
        self.memory_manager = None
        self.process_manager = None

    def connect_managers(self, file_manager, memory_manager, process_manager):
        self.file_manager = file_manager
        self.memory_manager = memory_manager
        self.process_manager = process_manager

    def status(self):
        print("Kernel status: Running")
        print(f"File Manager: {self.file_manager}")
        print(f"Memory Manager: {self.memory_manager}")
        print(f"Process Manager: {self.process_manager}")
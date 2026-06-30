class ProcessManager:
    def __init__(self):
        self.processes = []

    def create_process(self, name):
        self.processes.append(name)

    def list_processes(self):
        return self.processes
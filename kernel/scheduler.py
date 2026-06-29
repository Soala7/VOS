class ProcessManager:
    def __init__(self):
        self.processes = []

    def add_process(self, name):
        self.processes.append(name)

    def status(self):
        print("Processes:", self.processes)
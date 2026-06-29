class Memory_manager:
    def __init__(self):
        self.used_memory = 0
        self.total_memory = 1024  
    
    def status(self):
        return f"Used Memory: {self.used_memory} MB, Total Memory: {self.total_memory} MB"
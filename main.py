from kernel.memory import Memory_manager
from kernel.boot import BootLoader
from kernel.kernel import Kernel
from filesystem.filesystem import FileSystem
from kernel.scheduler import ProcessManager

boot = BootLoader()
boot.start()

kernel = Kernel()
file_manager = FileSystem()
memory = Memory_manager()
process_manager = ProcessManager()

kernel.connect_managers(file_manager, memory,process_manager)
kernel.status()
memory.status()
file_manager.status()
process_manager.status()


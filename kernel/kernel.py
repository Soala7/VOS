from core.services_manager import ServiceManager
from core.logger import Logger
from filesystem.filesystem import FileSystem
from process.manager import ProcessManager


class Kernel:
    def __init__(self):
        self.services_manager = ServiceManager()

    def boot(self):
        logger = Logger("Kernel")
        self.services_manager.register("logger", logger)

        logger.info("Boot sequence starting...")

        self._register_core_services()

        logger.info("Kernel boot complete.")

    def _register_core_services(self):
        sm = self.services_manager
        logger = sm.get("logger")

        sm.register("filesystem", FileSystem())
        sm.register("process", ProcessManager())

        logger.info("Core services registered.")
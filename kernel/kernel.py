from core.services_manager import ServiceManager
from core.logger import Logger
from core.event_bus import EventBus

from filesystem.filesystem import FileSystem
from process.manager import ProcessManager


class Kernel:
    def __init__(self):
        self.service_manager = ServiceManager()
        self.event_bus = EventBus()

    def boot(self):
        logger = Logger("Kernel")

        # Register core services first
        self.service_manager.register("logger", logger)
        self.service_manager.register("event_bus", self.event_bus)

        logger.info("Boot sequence starting...")

        # Register subsystems (event-aware)
        self._register_core_services()

        # Setup event listeners
        self._setup_event_system()

        logger.info("Kernel boot complete.")

    def _register_core_services(self):
        sm = self.service_manager
        logger = sm.get("logger")

        sm.register("filesystem", FileSystem(self.event_bus))
        sm.register("process", ProcessManager(self.event_bus))

        logger.info("Core services registered.")

    def _setup_event_system(self):
        bus = self.event_bus
        logger = self.service_manager.get("logger")

        def on_file_created(event):
            logger.info(f"File created: {event['data']['path']}")

        def on_file_deleted(event):
            logger.warning(f"File deleted: {event['data']['path']}")

        def on_process_started(event):
            logger.info(f"Process started: {event['data']['name']}")

        def on_process_terminated(event):
            logger.warning(f"Process terminated: {event['data']['name']}")

        bus.subscribe("file_created", on_file_created)
        bus.subscribe("file_deleted", on_file_deleted)
        bus.subscribe("process_started", on_process_started)
        bus.subscribe("process_terminated", on_process_terminated)

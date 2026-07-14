from datetime import datetime

from config.settings import Settings
from utils.logger import Logger


class BootManager:
    """Coordinates Kael's startup sequence."""

    def __init__(self) -> None:
        self.logger = Logger()
        self.settings: Settings | None = None
        self.module_names = ("Pulse", "Archive", "Echo", "Mind")

    def initialize(self) -> None:
        self.logger.info("Loading configuration")
        self.settings = Settings()
        self.logger.ok("Configuration loaded")

        self._print_header()

        self.logger.info("Initializing core modules")
        for module_name in self.module_names:
            self._initialize_module(module_name)

    def start(self) -> None:
        settings = self._require_settings()

        print()
        print("-" * 50)
        print()
        print(f"{self._greeting()}, {settings.user}.")
        print()
        print(f"Soy {settings.name}.")
        print()
        print("¿En qué trabajamos hoy?")
        print()

    def _print_header(self) -> None:
        settings = self._require_settings()

        print("=" * 50)
        print()
        print(f"        {settings.name.upper()}")
        print()
        print("Desktop AI Companion")
        print(f"Version {settings.version}")
        print()
        print("=" * 50)

    def _initialize_module(self, name: str) -> None:
        self.logger.ok(f"{name} initialized")

    def _greeting(self) -> str:
        hour = datetime.now().hour

        if 5 <= hour < 12:
            return "Buenos días"
        if 12 <= hour < 20:
            return "Buenas tardes"
        return "Buenas noches"

    def _require_settings(self) -> Settings:
        if self.settings is None:
            raise RuntimeError("BootManager must be initialized before start")

        return self.settings

from datetime import datetime

from config.settings import Settings
from utils.logger import Logger


def print_header(settings: Settings) -> None:
    print("=" * 50)
    print()
    print(f"        {settings.name.upper()}")
    print()
    print("Desktop AI Companion")
    print(f"Version {settings.version}")
    print()
    print("=" * 50)


def initialize_module(name: str, logger: Logger) -> None:
    logger.ok(f"{name} initialized")


def main() -> None:
    logger = Logger()

    logger.info("Loading configuration")
    settings = Settings()
    logger.ok("Configuration loaded")

    print_header(settings)

    logger.info("Initializing core modules")

    initialize_module("Pulse", logger)
    initialize_module("Archive", logger)
    initialize_module("Echo", logger)
    initialize_module("Mind", logger)

    print()
    print("-" * 50)
    print()

    hour = datetime.now().hour

    if 5 <= hour < 12:
        greeting = "Buenos días"
    elif 12 <= hour < 20:
        greeting = "Buenas tardes"
    else:
        greeting = "Buenas noches"

    print(f"{greeting}, {settings.user}.")
    print()
    print(f"Soy {settings.name}.")
    print()
    print("¿En qué trabajamos hoy?")
    print()


if __name__ == "__main__":
    main()

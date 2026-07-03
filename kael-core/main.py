from datetime import datetime

from config.settings import Settings

def print_header(settings: Settings) -> None:
    print("=" * 50)
    print()
    print(f"        {settings.name.upper()}")
    print()
    print("Desktop AI Companion")
    print(f"Version {settings.version}")
    print()
    print("=" * 50)


def initialize_module(name: str) -> None:
    print(f"[OK] {name} initialized")


def main() -> None:
    settings = Settings()

    print_header(settings)

    print("Initializing...")
    print()

    initialize_module("Pulse")
    initialize_module("Archive")
    initialize_module("Echo")
    initialize_module("Mind")

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

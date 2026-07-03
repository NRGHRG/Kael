from datetime import datetime


VERSION = "0.0.1"
USER_NAME = "Memo"


def print_header():
    print("=" * 50)
    print()
    print("        K A E L")
    print()
    print("Desktop AI Companion")
    print(f"Version {VERSION}")
    print()
    print("=" * 50)


def initialize_module(name: str):
    print(f"✓ {name} initialized")


def main():
    print_header()

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

    print(f"{greeting}, {USER_NAME}.")
    print()
    print("Soy Kael.")
    print()
    print("¿En qué trabajamos hoy?")
    print()


if __name__ == "__main__":
    main()
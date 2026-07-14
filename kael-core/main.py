from boot.manager import BootManager


def main() -> None:
    boot = BootManager()
    boot.initialize()
    boot.start()


if __name__ == "__main__":
    main()

from datetime import datetime


class Logger:
    """Small console logger for Kael startup and operational messages."""

    def _log(self, level: str, message: str) -> None:
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}][{level}] {message}")

    def info(self, message: str) -> None:
        self._log("INFO", message)

    def ok(self, message: str) -> None:
        self._log("OK", message)

    def warn(self, message: str) -> None:
        self._log("WARN", message)

    def error(self, message: str) -> None:
        self._log("ERROR", message)

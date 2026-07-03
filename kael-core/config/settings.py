from pathlib import Path
import json
from typing import Any


class Settings:
    def __init__(self) -> None:
        config_path = Path(__file__).parent / "config.json"

        with config_path.open(encoding="utf-8") as file:
            self.data = json.load(file)

        self.name = self._require("name", str)
        self.user = self._require("user", str)
        self.language = self._require("language", str)
        self.version = self._require("version", str)
        self.voice_enabled = self._require("voice_enabled", bool)
        self.debug = self._require("debug", bool)

    def _require(self, key: str, expected_type: type) -> Any:
        if key not in self.data:
            raise ValueError(f"Missing required setting: {key}")

        value = self.data[key]
        if not isinstance(value, expected_type):
            raise TypeError(
                f"Setting '{key}' must be {expected_type.__name__}, "
                f"not {type(value).__name__}"
            )

        return value

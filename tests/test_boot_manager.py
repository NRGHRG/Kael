import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CORE_PATH = PROJECT_ROOT / "kael-core"
sys.path.insert(0, str(CORE_PATH))

from boot.manager import BootManager  # noqa: E402


class BootManagerTest(unittest.TestCase):
    def test_initialize_loads_settings_and_initializes_modules(self) -> None:
        boot = BootManager()
        stream = io.StringIO()

        with redirect_stdout(stream):
            boot.initialize()

        output = stream.getvalue()

        self.assertIsNotNone(boot.settings)
        self.assertIn("[INFO] Loading configuration", output)
        self.assertIn("[OK] Configuration loaded", output)
        self.assertIn("KAEL", output)
        self.assertIn("[INFO] Initializing core modules", output)
        self.assertIn("[OK] Pulse initialized", output)
        self.assertIn("[OK] Archive initialized", output)
        self.assertIn("[OK] Echo initialized", output)
        self.assertIn("[OK] Mind initialized", output)

    def test_start_requires_initialize_first(self) -> None:
        boot = BootManager()

        with self.assertRaisesRegex(
            RuntimeError,
            "BootManager must be initialized before start",
        ):
            boot.start()

    def test_start_prints_ready_prompt_after_initialize(self) -> None:
        boot = BootManager()
        stream = io.StringIO()

        with redirect_stdout(stream):
            boot.initialize()
            boot.start()

        output = stream.getvalue()

        self.assertIn("Memo.", output)
        self.assertIn("Soy Kael.", output)
        self.assertIn("¿En qué trabajamos hoy?", output)


if __name__ == "__main__":
    unittest.main()

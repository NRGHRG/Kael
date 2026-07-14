import io
import re
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CORE_PATH = PROJECT_ROOT / "kael-core"
sys.path.insert(0, str(CORE_PATH))

from utils.logger import Logger  # noqa: E402


class LoggerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.logger = Logger()

    def assert_log_output(self, method_name: str, level: str) -> None:
        stream = io.StringIO()
        message = f"{level.lower()} message"

        with redirect_stdout(stream):
            getattr(self.logger, method_name)(message)

        output = stream.getvalue()
        pattern = rf"^\[\d{{2}}:\d{{2}}:\d{{2}}\]\[{level}\] {message}\n$"
        self.assertRegex(output, re.compile(pattern))

    def test_info_logs_info_level(self) -> None:
        self.assert_log_output("info", "INFO")

    def test_ok_logs_ok_level(self) -> None:
        self.assert_log_output("ok", "OK")

    def test_warn_logs_warn_level(self) -> None:
        self.assert_log_output("warn", "WARN")

    def test_error_logs_error_level(self) -> None:
        self.assert_log_output("error", "ERROR")


if __name__ == "__main__":
    unittest.main()

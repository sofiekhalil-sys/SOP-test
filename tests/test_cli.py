import io
import unittest
from contextlib import redirect_stdout

from sop_test import main


class MainTests(unittest.TestCase):
    def test_main_prints_greeting_and_returns_success(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            result = main()

        self.assertEqual(result, 0)
        self.assertEqual(output.getvalue(), "Hello from sop-test!\n")


if __name__ == "__main__":
    unittest.main()

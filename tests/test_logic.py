import subprocess
import sys
import unittest
from pathlib import Path
SRC = Path(__file__).resolve().parents[1] / "src"
class DemoProgramTests(unittest.TestCase):
    def test_normal_program_finishes(self):
        result = subprocess.run([sys.executable, str(SRC/"normal_program.py")], capture_output=True, text=True, timeout=2)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Program completed successfully.", result.stdout)
    def test_error_program_exits_nonzero(self):
        result = subprocess.run([sys.executable, str(SRC/"error_program.py")], capture_output=True, text=True, timeout=2)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ValueError", result.stderr)
if __name__ == "__main__": unittest.main()

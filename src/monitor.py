"""CLI timeout monitor for the predefined sample programs."""
import argparse
import subprocess
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
CASES = {"normal": ROOT/"normal_program.py", "infinite": ROOT/"infinite_program.py", "error": ROOT/"error_program.py"}
def run(path, timeout):
    try:
        result = subprocess.run([sys.executable, str(path)], cwd=str(ROOT), capture_output=True, text=True, timeout=timeout)
        print(result.stdout)
        if result.returncode == 0: print("STATUS: PROGRAM COMPLETED")
        else: print("STATUS: PROGRAM EXITED WITH ERROR", result.stderr)
    except subprocess.TimeoutExpired:
        print("STATUS: POSSIBLE NON-TERMINATING BEHAVIOUR — TIMEOUT")
        print("A timeout does not prove an infinite loop.")
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=["all", *CASES], default="all")
    parser.add_argument("--timeout", type=float, default=3.0)
    args = parser.parse_args()
    selected = CASES if args.case == "all" else {args.case: CASES[args.case]}
    for name, path in selected.items():
        print("\nChecking:", name)
        run(path, args.timeout)
if __name__ == "__main__": main()

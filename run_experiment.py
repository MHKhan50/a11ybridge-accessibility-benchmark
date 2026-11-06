#!/usr/bin/env python3
"""Run the A11yBridge synthetic Playwright benchmark."""
import argparse
import json
from pathlib import Path

from a11ybridge.benchmark import run_benchmark


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="results", help="directory for CSV and JSON outputs")
    parser.add_argument("--repetitions", type=int, default=1, help="repetitions per task/variant pair")
    parser.add_argument("--headless", choices=("true", "false"), default="true")
    args = parser.parse_args()
    summary = run_benchmark(Path(args.output_dir), args.repetitions, args.headless == "true")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

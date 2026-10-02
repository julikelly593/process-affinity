"""Process Affinity — Pin a process to selected CPU cores and save the profile for next launch."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='process_affinity',
        description='Pin a process to selected CPU cores and save the profile for next launch.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Process Affinity')
    print('CPU affinity without the Task Manager dialog.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

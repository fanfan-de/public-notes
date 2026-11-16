#!/usr/bin/env python3
"""Locate this skill's notes clone independently of the caller's working directory."""

from pathlib import Path
import subprocess
from urllib.parse import urlsplit


def main():
    root = Path(__file__).resolve().parents[4]
    result = subprocess.run(["git", "-C", str(root), "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    if result.returncode or Path(result.stdout.strip()).resolve() != root:
        raise SystemExit("Run scripts/setup.py in the intended public-notes clone to register this skill.")
    result = subprocess.run(["git", "-C", str(root), "remote", "get-url", "origin"], capture_output=True, text=True)
    if result.returncode:
        raise SystemExit("The notes clone needs its GitHub origin configured before this skill can locate it.")
    remote = result.stdout.strip()
    if remote.startswith("git@"):
        remote = "ssh://" + remote.replace(":", "/", 1)
    url = urlsplit(remote)
    if url.hostname != "github.com" or url.path.strip("/").removesuffix(".git").lower() != "fanfan-de/public-notes":
        raise SystemExit("This skill is not attached to the expected public-notes clone; run setup in the correct clone.")
    if not (root / "AGENTS.md").is_file() or not (root / "README.md").is_file():
        raise SystemExit("The notes clone is missing its repository instructions or index.")
    print(root)


if __name__ == "__main__":
    main()

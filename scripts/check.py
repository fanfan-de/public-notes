#!/usr/bin/env python3
"""Check the Git index, then scan staged changes or all history for secrets."""

import argparse
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys

MAX_BYTES = 1024 * 1024
IMAGE_TYPES = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
PRIVATE_DIRS = {".obsidian", ".trash", ".private", "private", "secrets"}
BLOCKED_TYPES = {
    ".pem", ".key", ".p12", ".pfx", ".kdbx", ".har", ".log", ".jsonl",
    ".sqlite", ".sqlite3", ".db", ".pdf", ".zip", ".7z", ".rar", ".tar",
    ".gz", ".mp4", ".mov", ".mkv", ".mp3", ".wav", ".m4a",
}


def git(*args):
    return subprocess.check_output(["git", *args])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--history", action="store_true", help="scan all local Git refs")
    args = parser.parse_args()
    root = Path(os.fsdecode(git("rev-parse", "--show-toplevel")).strip())
    os.chdir(root)
    problems = []
    entries = git("ls-files", "--stage", "-z").split(b"\0")
    count = 0
    for entry in filter(None, entries):
        meta, raw_path = entry.split(b"\t", 1)
        mode, oid, stage = meta.split()
        name = os.fsdecode(raw_path)
        path = PurePosixPath(name)
        parts = {part.lower() for part in path.parts}
        suffix = path.suffix.lower()
        count += 1
        if stage != b"0":
            problems.append(f"{name}: unresolved merge conflict")
            continue
        if mode not in (b"100644", b"100755"):
            problems.append(f"{name}: symlinks and submodules are not allowed")
            continue
        if parts & PRIVATE_DIRS or any(part.lower().startswith(".env") for part in path.parts):
            problems.append(f"{name}: private or local-only path")
            continue
        if suffix in BLOCKED_TYPES:
            problems.append(f"{name}: private export or heavy attachment type")
            continue
        size = int(git("cat-file", "-s", oid.decode()))
        if size > MAX_BYTES:
            problems.append(f"{name}: {size} bytes exceeds the 1 MiB limit")
            continue
        if suffix not in IMAGE_TYPES:
            data = git("cat-file", "blob", oid.decode())
            try:
                data.decode("utf-8")
                if b"\0" in data:
                    raise UnicodeError("NUL in text")
            except UnicodeError:
                problems.append(f"{name}: unsupported binary file; use a public source link")
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1
    managed = Path.home() / ".local" / "bin" / "gitleaks"
    scanner = str(managed) if managed.is_file() else shutil.which("gitleaks")
    if not scanner:
        print("Gitleaks missing. Run: python3 scripts/setup.py", file=sys.stderr)
        return 1
    command = [scanner, "git", "--config", str(root / ".gitleaks.toml"),
               "--redact", "--no-banner", "--no-color", "--ignore-gitleaks-allow"]
    command += ["--log-opts=--all"] if args.history else ["--pre-commit", "--staged"]
    result = subprocess.run(command)
    if result.returncode:
        return result.returncode
    print(f"Checked {count} indexed files: size, paths, types and secret scan passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

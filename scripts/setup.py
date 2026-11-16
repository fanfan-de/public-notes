#!/usr/bin/env python3
"""Install local checks and register the cross-project public-note skill."""

import argparse
import hashlib
import io
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tarfile
import urllib.request

VERSION = "8.30.1"


def install_note_skill(root):
    source = root / ".agents" / "skills" / "save-public-note"
    if not (source / "SKILL.md").is_file():
        raise SystemExit("The notes clone is missing the save-public-note skill.")
    destination = Path.home() / ".agents" / "skills" / "save-public-note"
    if destination.is_symlink():
        if destination.resolve() == source.resolve():
            return destination
        if destination.exists():
            raise SystemExit("save-public-note already points to another clone; select the intended clone before changing it.")
        destination.unlink()
    elif destination.exists():
        raise SystemExit("A user skill named save-public-note already exists; it has not been overwritten.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.symlink_to(source.resolve(), target_is_directory=True)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checks-only", action="store_true", help="set up checks without registering a user-global skill")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    git_root = Path(subprocess.check_output(["git", "-C", str(root), "rev-parse", "--show-toplevel"], text=True).strip()).resolve()
    if git_root != root:
        raise SystemExit("Run this setup script from a complete public-notes Git clone.")
    target = Path.home() / ".local" / "bin" / "gitleaks"
    installed = str(target) if target.is_file() else shutil.which("gitleaks")
    current = subprocess.check_output([installed, "version"], text=True).strip() if installed else ""
    if current != VERSION:
        system = platform.system().lower()
        arch = {"x86_64": "x64", "amd64": "x64", "aarch64": "arm64", "arm64": "arm64"}.get(platform.machine().lower())
        if system not in ("linux", "darwin") or not arch:
            raise SystemExit(f"Install Gitleaks {VERSION} manually for this platform, then run setup again.")
        name = f"gitleaks_{VERSION}_{system}_{arch}.tar.gz"
        base = f"https://github.com/gitleaks/gitleaks/releases/download/v{VERSION}/"
        with urllib.request.urlopen(base + name, timeout=60) as response:
            archive = response.read()
        with urllib.request.urlopen(base + f"gitleaks_{VERSION}_checksums.txt", timeout=30) as response:
            checksums = response.read().decode()
        expected = next(line.split()[0] for line in checksums.splitlines() if line.split()[-1] == name)
        if hashlib.sha256(archive).hexdigest() != expected:
            raise SystemExit("Gitleaks download failed SHA-256 verification.")
        with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as bundle:
            binary = bundle.extractfile("gitleaks").read()
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_name("gitleaks.download")
        temporary.write_bytes(binary)
        temporary.chmod(0o755)
        temporary.replace(target)
    for name in ("pre-commit", "pre-push"):
        (root / ".githooks" / name).chmod(0o755)
    subprocess.run(["git", "-C", str(root), "config", "--local", "core.hooksPath", ".githooks"], check=True)
    print(f"Gitleaks {VERSION} ready; pre-commit and pre-push hooks enabled for this clone.")
    if not args.checks_only:
        destination = install_note_skill(root)
        print(f"Cross-project skill registered: {destination}")


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Install a verified Gitleaks release and enable this clone's Git hooks."""

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


def main():
    root = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
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
    subprocess.run(["git", "config", "--local", "core.hooksPath", ".githooks"], check=True)
    print(f"Gitleaks {VERSION} ready; pre-commit and pre-push hooks enabled for this clone.")


if __name__ == "__main__":
    sys.exit(main())

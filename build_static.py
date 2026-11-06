#!/usr/bin/env python3
"""Package only the local server's allowlisted site files for Vercel."""
import json
import runpy
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def main():
    subprocess.run([sys.executable, "-B", str(ROOT / "render_guides.py")], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "-B", str(ROOT / "check_navigation.py")], cwd=ROOT, check=True)
    files = runpy.run_path(str(ROOT / "server.py"))["FILES"]
    output = ROOT / ".vercel" / "output"
    if output.exists():
        shutil.rmtree(output)
    static = output / "static"
    static.mkdir(parents=True)
    for filename in sorted({entry[0] for entry in files.values()}):
        destination = static / filename
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / filename, destination)
    config = {
        "version": 3,
        "overrides": {
            filename: {"contentType": media}
            for filename, media in files.values()
            if filename.endswith(".md")
        },
        "routes": [
            {
                "src": "/(.*)",
                "headers": {
                    "Content-Security-Policy": "default-src 'none'; style-src 'self'; script-src 'none'; base-uri 'none'; frame-ancestors 'none'",
                    "X-Content-Type-Options": "nosniff",
                    "Cache-Control": "public, max-age=0, must-revalidate",
                },
                "continue": True,
            },
            {"handle": "filesystem"},
            {"src": "/.*", "status": 404},
        ],
    }
    (output / "config.json").write_text(json.dumps(config, indent=2) + "\n")
    print(f"Packaged {len(set(entry[0] for entry in files.values()))} public files in {static}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

for folder in [
    ROOT / "notes" / "daily",
    ROOT / "notes" / "weekly",
    ROOT / "notes" / "interview_prep",
    ROOT / "docs",
    ROOT / "projects",
    ROOT / "leetcode",
]:
    folder.mkdir(parents=True, exist_ok=True)

print("Repository folders ensured.")

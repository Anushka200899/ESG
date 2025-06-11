#!/usr/bin/env python3
"""
repo_cleanup.py  –  one-shot script to consolidate docs/tools
Author: ChatGPT   |   Run from the repo root.
"""

import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAPER = ROOT / "ESG_Indigenous_Economies_Paper"

def safe_rename(src: Path, dst: Path):
    if src.exists():
        print(f"Renaming {src} -> {dst}")
        src.rename(dst)
    else:
        print(f"[skip] {src} not found")

def move_new_rti_tracker():
    src = ROOT / "Filed_RTIs_Final_Format.xlsx"
    dst_dir = PAPER / "03_RTI_Tracking"
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / "Filed_RTIs_Final_Format.xlsx"

    if not src.exists():
        print("[skip] new RTI tracker not found in repo root")
        return
    # Delete old if present
    old = dst_dir / "Filed_RTIs.xlsx"
    if old.exists():
        print("Removing outdated RTI tracker:", old.name)
        old.unlink()
    print("Copying new RTI tracker ->", dst.relative_to(ROOT))
    shutil.copy2(src, dst)

def patch_readme():
    readme = PAPER / "README.md"
    if not readme.exists():
        print("[skip] README.md not found")
        return
    txt = readme.read_text(encoding="utf-8")
    new_txt = re.sub(r"06_Docs/?", "tools/", txt)
    if txt != new_txt:
        readme.write_text(new_txt, encoding="utf-8")
        print("README.md paths updated → tools/")
    else:
        print("README.md already points to tools/")

def main():
    tools_dir = PAPER / "tools"
    # 1. rename 06_Docs → tools
    safe_rename(PAPER / "06_Docs", tools_dir)

    # 2. fix rubric filename typo
    typo = tools_dir / "ESG_SCoring_Rubric.xlsx"
    correct = tools_dir / "ESG_Scoring_Rubric.xlsx"
    safe_rename(typo, correct)

    # 3. replace RTI tracker
    move_new_rti_tracker()

    # 4. update README paths
    patch_readme()

    print("\nCleanup done. Review changes, then:")
    print("    git add ESG_Indigenous_Economies_Paper")
    print('    git commit -m "chore: consolidate docs into tools, update RTI tracker & README"')

if __name__ == "__main__":
    main()

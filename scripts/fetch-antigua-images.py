#!/usr/bin/env python3
"""Download images from Wikimedia Commons for Antigua site."""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

# (filename, url, source_note)
DOWNLOADS: list[tuple[str, str, str]] = [
    ("hero-antigua.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Dickinson_bay_beach_antigua.jpg/1920px-Dickinson_bay_beach_antigua.jpg",
     "Wikimedia: Dickenson Bay beach, Antigua"),
    ("antigua-cruise-port.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/St._John%27s_Antigua_Cruise_Port_1.jpg/1920px-St._John%27s_Antigua_Cruise_Port_1.jpg",
     "Wikimedia: St John's Antigua cruise port"),
    ("antigua-port-arrival.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/St._John%27s_Antigua_Cruise_Port_2.jpg/1920px-St._John%27s_Antigua_Cruise_Port_2.jpg",
     "Wikimedia: St John's harbour cruise port"),
    ("antigua-intro.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Antigua_und_Barbuda_-_panoramio_-_georama_%2837%29.jpg/1920px-Antigua_und_Barbuda_-_panoramio_-_georama_%2837%29.jpg",
     "Wikimedia: Antigua coastline panorama"),
    ("best-antigua-excursions.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Nelson%27s_Dockyard_Antigua.jpg/1920px-Nelson%27s_Dockyard_Antigua.jpg",
     "Wikimedia: Nelson's Dockyard Antigua"),
    ("one-day-antigua.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Antigua_Shirley_Heights.JPG/1920px-Antigua_Shirley_Heights.JPG",
     "Wikimedia: Shirley Heights Antigua"),
    ("the-antiguan-experience.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Antigua_und_Barbuda_-_panoramio_-_georama_%2836%29.jpg/1920px-Antigua_und_Barbuda_-_panoramio_-_georama_%2836%29.jpg",
     "Wikimedia: Antigua countryside scenery"),
    ("classic-beach-day.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Dickinson_bay_beach_antigua.jpg/1920px-Dickinson_bay_beach_antigua.jpg",
     "Wikimedia: Dickenson Bay white sand beach Antigua"),
    ("antigua-kayak-snorkel.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Kayaking_the_mangrove_in_Isla_de_Damas_-_panoramio.jpg/1920px-Kayaking_the_mangrove_in_Isla_de_Damas_-_panoramio.jpg",
     "Wikimedia: Mangrove kayaking (illustrative for Cades Bay)"),
    ("history-culture-tour.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Antigua_-_English_Harbour%2C_Nelsons_Dockyard_-_panoramio.jpg/1920px-Antigua_-_English_Harbour%2C_Nelsons_Dockyard_-_panoramio.jpg",
     "Wikimedia: Nelson's Dockyard English Harbour Antigua"),
    ("panoramic-antigua.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Antigua_Shirley_Heights.JPG/1920px-Antigua_Shirley_Heights.JPG",
     "Wikimedia: Shirley Heights panoramic view Antigua"),
    ("half-day-kayak-snorkel.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Kayaking_the_mangrove_in_Isla_de_Damas_-_panoramio.jpg/1920px-Kayaking_the_mangrove_in_Isla_de_Damas_-_panoramio.jpg",
     "Wikimedia: Mangrove lagoon kayaking (illustrative)"),
    ("nelsons-dockyard.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Nelson%27s_Dockyard_Antigua.jpg/1920px-Nelson%27s_Dockyard_Antigua.jpg",
     "Wikimedia: Nelson's Dockyard Antigua UNESCO site"),
    ("shirley-heights.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Antigua_Shirley_Heights.JPG/1920px-Antigua_Shirley_Heights.JPG",
     "Wikimedia: Shirley Heights lookout Antigua"),
    ("antigua-beaches.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Sea_Grapes_Beach%2C_Hawksbill_Bay%2C_Antigua.jpg/1920px-Sea_Grapes_Beach%2C_Hawksbill_Bay%2C_Antigua.jpg",
     "Wikimedia: Sea Grapes Beach Hawksbill Bay Antigua"),
    ("cades-reef.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Buck_Island_Reef_National_Monument%2C_Virgin_Islands_%2806523f05-6c64-4c00-abe8-c14d9a46efab%29.jpg/1920px-Buck_Island_Reef_National_Monument%2C_Virgin_Islands_%2806523f05-6c64-4c00-abe8-c14d9a46efab%29.jpg",
     "Wikimedia: Caribbean reef snorkelling (illustrative for Cades Reef)"),
]


def download(filename: str, url: str, note: str) -> bool:
    dest = IMAGES / filename
    print(f"  {filename}")
    print(f"    {note}")
    result = subprocess.run(
        ["curl", "-fsSL", "-o", str(dest), url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"    FAILED: {result.stderr.strip()}", file=sys.stderr)
        return False
    size = dest.stat().st_size
    if size < 10_000:
        print(f"    WARNING: small file ({size} bytes)", file=sys.stderr)
    print(f"    OK ({size // 1024} KB)")
    return True


def main() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    print("Downloading Antigua images…")
    failed = 0
    for i, (filename, url, note) in enumerate(DOWNLOADS):
        if i:
            time.sleep(1.5)
        if not download(filename, url, note):
            failed += 1
    if failed:
        raise SystemExit(f"{failed} download(s) failed.")
    print("Done.")


if __name__ == "__main__":
    main()

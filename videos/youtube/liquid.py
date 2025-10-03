import os
import glob

def update_layouts():
    # Get all .html files in the current folder only
    files = sorted(glob.glob("*.html"))
    layout_num = 0

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if not lines:
            continue

        for idx, line in enumerate(lines):
            if line.strip().startswith("layout: video"):
                new_layout = f"layout: video-{layout_num:02d}\n"
                lines[idx] = new_layout
                print(f"Updated {file_path} → {new_layout.strip()}")
                break

        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

        layout_num = (layout_num + 1) % 10  # cycle from 00 → 09

if __name__ == "__main__":
    update_layouts()

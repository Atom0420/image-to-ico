#!/usr/bin/env python3
import sys
from pathlib import Path
from PIL import Image

SUPPORTED_EXTS = {".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff"}

def convert_to_ico(input_path: Path, output_dir: Path):
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")
        output_path = output_dir / (input_path.stem + ".ico")
        img.save(
            output_path,
            format="ICO",
            sizes=[(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)]
        )
        print(f"[OK] {input_path.name} → {output_path.name}")
    except Exception as e:
        print(f"[ERR] Could not convert {input_path.name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Drag and drop image files onto this script to convert them.")
        sys.exit(1)

    # Directory where the script itself is located
    script_dir = Path(__file__).resolve().parent

    for arg in sys.argv[1:]:
        file = Path(arg)
        if file.suffix.lower() in SUPPORTED_EXTS:
            convert_to_ico(file, script_dir)
        else:
            print(f"[SKIP] {file.name} (unsupported format)")


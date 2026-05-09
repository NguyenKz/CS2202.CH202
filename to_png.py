import sys
from pathlib import Path

from PIL import Image
from pillow_heif import register_heif_opener


if len(sys.argv) != 2:
    print("Usage: python to_png.py <input_path>")
    sys.exit(1)

register_heif_opener()

input_path = sys.argv[1]
output_path = Path(input_path).with_suffix(".png")

img = Image.open(input_path)
img.save(output_path)
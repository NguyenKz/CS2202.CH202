import sys
from pathlib import Path

from PIL import Image
from pillow_heif import register_heif_opener


if len(sys.argv) != 2:
    print("Usage: python to_png.py <input_path>")
    sys.exit(1)

register_heif_opener()


def convert_to_png(input_path: Path) -> None:
    if input_path.suffix.lower() == ".png":
        return

    output_path = input_path.with_suffix(".png")
    if output_path.exists():
        return

    img = Image.open(input_path)
    img.save(output_path)
    print(f"Converted: {input_path} -> {output_path}")


input_path = Path(sys.argv[1])

if input_path.is_dir():
    for file_path in input_path.iterdir():
        if file_path.is_file():
            convert_to_png(file_path)
else:
    convert_to_png(input_path)
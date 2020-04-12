from pathlib import Path
from datetime import datetime

from pyexiv2 import ImageMetadata


def get_datetime_of_image(img_path: Path) -> datetime:
    meta = ImageMetadata(str(img_path))
    meta.read()
    return meta.get("Exif.Image.DateTime").value

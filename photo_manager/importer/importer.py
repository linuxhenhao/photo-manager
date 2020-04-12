from typing import List
import pathlib
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os

from photo_manager.model import models
from . import exif


class Importer:
    def __init__(self, src_root: str):
        self._src_dir_path = pathlib.Path(src_root)
        self._suffixes = {"mp4", "mov", "jpg", "jpeg", "png"}
        self._thread_pool_executor = ThreadPoolExecutor(max_workers=200)
        self._process_pool_executor = ProcessPoolExecutor(max_workers=os.cpu_count())

    async def import_photos(self):
        pass

    async def get_images(self) -> List[pathlib.Path]:
        return self._get_images(self._src_dir_path)

    def _get_images(self, dir_path: pathlib.Path) -> List[pathlib.Path]:
        images = list()
        for item in dir_path.iterdir():
            if item.is_dir():
                images.extend(self._get_images(item))
            else:
                if self._should_include(item):
                    images.append(item)
        return images

    def _should_include(self, path: pathlib.Path) -> bool:
        return path.suffix.lower() in self._suffixes

    def get_photos(self, image_paths: List[pathlib.Path]) -> List[models.Photo]:
        for image_path in image_paths:
            pass

    def get_photo(self, image_path: pathlib.Path) -> models.Photo:
        path = str(image_path.relative_to(self._src_dir_path))
        size = image_path.lstat().st_size
        md5sum = self._process_pool_executor.submit()
        create_time = exif.get_datetime_of_image(image_path)


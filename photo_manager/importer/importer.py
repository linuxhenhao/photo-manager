from typing import List
import pathlib

from photo_manager.model import models


class Importer:
    def __init__(self, src_root: str):
        self._src_root = src_root

    async def import_photos(self):
        pass

    async def _get_images(self) -> List[pathlib.Path]:
        pass

    async def _get_photos(self) -> List[models.Photo]:
        pass

from sqlalchemy import create_engine
from sqlalchemy.orm import session

from photo_manager.model import models


class Storage:
    def __init__(self, db_url: str, storage_root: str):
        """
        :param db_url:
        :param storage_root: images are stored in relative to storage_root
        """
        self._session = self._create_session(db_url)
        self._storage_root = storage_root

    @staticmethod
    def _create_session(db_url: str) -> session.Session:
        engine = create_engine(db_url)
        session_ = session.sessionmaker()(bind=engine)
        return session_

    def add(self, photo: models.Photo) -> None:
        pass

    def delete(self, photo: models.Photo) -> None:
        pass

    def _add_file(self, photo_src: str) -> None:
        pass

    def _add2db(self, photo: models.Photo) -> None:
        pass

    def _del_file(self, photo_loc: str) -> None:
        pass

    def _del_dbinfo(self, photo: models.Photo) -> None:
        pass

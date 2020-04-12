import dataclasses
from datetime import datetime
from typing import TypeVar, Type, Optional

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    ForeignKeyConstraint,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
T = TypeVar("T")


@dataclasses.dataclass
class Photo:
    src_path: str
    relative_path: str
    size: int
    create_time: datetime


class PhotoModel(Base):
    __tablename__ = "photo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    path = Column(String(500), nullable=False, index=True)
    size = Column(Integer, nullable=False)
    md5sum = Column(String(32), nullable=False, index=True)
    meta_info_path = Column(String(500), nullable=False)  # position of exif info json
    create_time = Column(DateTime, nullable=False)
    data: bytes

    @classmethod
    def from_photo(cls: Type[T], photo: Photo) -> Optional[T]:
        # TODO:
        # read in photo, calculate md5sum, check in db,
        with open(photo.src_path, "br") as f:
            photo_data = f.read()
        instance = cls(
            path=photo.relative_path,
            size=photo.size,
            create_time=photo.create_time,
        )
        instance.data = photo_data
        return instance


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)


class PhotoTag(Base):
    __tablename__ = "photo_tag"

    photo_id = Column(
        Integer,
        ForeignKey("photo.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=True,
        primary_key=True,
        index=True,
    )
    tag_id = Column(
        Integer,
        ForeignKey("tag.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=True,
        primary_key=True,
        index=True,
    )


class Thumbnail(Base):
    __tablename__ = "thumbnail"

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo_id = Column(
        Integer,
        ForeignKey("photo.id"),
        ForeignKeyConstraint(ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    name = Column(String(32), nullable=False)


def create_database(db_url: str) -> None:
    engine = create_engine(db_url)
    Photo.metadata.create_all(engine)
    Tag.metadata.create_all(engine)
    PhotoTag.metadata.create_all(engine)
    Thumbnail.metadata.create_all(engine)

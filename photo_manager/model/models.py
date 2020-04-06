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


class Photo(Base):
    __tablename__ = "photo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    path = Column(String(500), nullable=False, index=True)
    size = Column(Integer, nullable=False)
    md5sum = Column(String(32), nullable=False, index=True)
    create_time = Column(DateTime, nullable=False)


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

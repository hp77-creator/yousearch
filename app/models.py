from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class VideoMetaData(Base):
    __tablename__ = "videometadata"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    published_date = Column(DateTime)
    thumbnail_url = Column(String)
    channel_url = Column(String)
    channel_title = Column(String, nullable=True)

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Float, String


class Base(DeclarativeBase):
    pass


class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True)

    rank = Column(Integer)

    channel_name = Column(String)

    genre = Column(String)

    subscriber_count = Column(Float)

    video_views = Column(Float)

    video_count = Column(Float)

    channel_age = Column(Float)

    health_score = Column(Float)

    growth_score = Column(Float)

    creator_segment = Column(String)
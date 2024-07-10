from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Song(Base):
    __tablename__ = "songs"

    id = Column(String, primary_key=True, index=True, nullable=False)
    title = Column(String, index=True, nullable=False)
    danceability = Column(Float, nullable=False)
    energy = Column(Float, nullable=False)
    key = Column(Integer, nullable=False)
    loudness = Column(Float, nullable=False)
    mode = Column(Integer, nullable=False)
    acousticness = Column(Float, nullable=False)
    instrumentalness = Column(Float, nullable=False)
    liveness = Column(Float, nullable=False)
    valence = Column(Float, nullable=False)
    tempo = Column(Float, nullable=False)
    duration_ms = Column(Integer, nullable=False)
    time_signature = Column(Integer, nullable=False)
    num_bars = Column(Integer, nullable=False)
    num_sections = Column(Integer, nullable=False)
    num_segments = Column(Integer, nullable=False)
    _class = Column("class", Integer, nullable=False)
    rating = Column(Integer, nullable=False)

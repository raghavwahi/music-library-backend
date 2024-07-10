"""
SQLAlchemy model for representing songs.

This model defines the schema for the `songs` table in the database, including various attributes
for each song.

Attributes:
    - id (str): Primary key identifier of the song.
    - title (str): Title of the song.
    - danceability (float): Danceability score of the song.
    - energy (float): Energy score of the song.
    - key (int): Key of the song.
    - loudness (float): Loudness level of the song.
    - mode (int): Mode of the song.
    - acousticness (float): Acousticness score of the song.
    - instrumentalness (float): Instrumentalness score of the song.
    - liveness (float): Liveness score of the song.
    - valence (float): Valence score of the song.
    - tempo (float): Tempo of the song.
    - duration_ms (int): Duration of the song in milliseconds.
    - time_signature (int): Time signature of the song.
    - num_bars (int): Number of bars in the song.
    - num_sections (int): Number of sections in the song.
    - num_segments (int): Number of segments in the song.
    - class_ (int): Class of the song (aliased to 'class' due to Python keyword).
    - rating (int): Rating of the song.

Example usage:
    song = Song(
        id="1",
        title="Example Song",
        danceability=0.8,
        energy=0.7,
        key=2,
        loudness=-5.2,
        mode=1,
        acousticness=0.2,
        instrumentalness=0.0,
        liveness=0.5,
        valence=0.9,
        tempo=120.0,
        duration_ms=240000,
        time_signature=4,
        num_bars=64,
        num_sections=8,
        num_segments=200,
        class_=1,
        rating=5
    )
"""

from sqlalchemy import Column, Float, Integer, String
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
    class_ = Column(Integer, name="class", nullable=False)
    rating = Column(Integer, nullable=False)

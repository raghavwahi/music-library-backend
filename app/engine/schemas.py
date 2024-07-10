"""
Pydantic models for representing songs and song pagination data.

These models define the structure and validation rules for songs and paginated song data used in the application.

Models:
    - Song: Represents a single song with various attributes.
    - SongPagination: Represents paginated song data including total count, skip, limit, and a list of songs.

Example:
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

Attributes:
    - id (str): Identifier of the song.
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

Note:
    - `class_` attribute is aliased to `class` using `Field` for compatibility with Python keywords.

"""

from typing import List

from pydantic import BaseModel, Field


class Song(BaseModel):
    id: str
    title: str
    danceability: float
    energy: float
    key: int
    loudness: float
    mode: int
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    duration_ms: int
    time_signature: int
    num_bars: int
    num_sections: int
    num_segments: int
    class_: int = Field(..., alias="class")
    rating: int

    class Config:
        orm_mode: True
        populate_by_name = True
        from_attributes = True


class SongPagination(BaseModel):
    total: int
    skip: int
    limit: int
    data: List[Song]

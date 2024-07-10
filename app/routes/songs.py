"""
Songs API Router module for handling CRUD operations on songs.

This module defines routes and handlers for interacting with songs in the database using FastAPI.
It includes endpoints for retrieving songs, updating a song by ID, and getting a song by its title.

Endpoints:
    - GET /songs: Retrieve a list of songs with pagination support.
    - GET /songs/{title}: Retrieve a song by its title (case-insensitive).
    - PUT /songs/{song_id}: Update a song by its ID.

Usage:
    This module is typically included in a FastAPI application using `include_router()` method.

Example:
    from fastapi import FastAPI
    from app.routes import songs

    app = FastAPI()

    # Include songs router
    app.include_router(songs.router)
"""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.engine import database, models, schemas

router = APIRouter(prefix="/songs", tags=["songs"])


@router.get("/", response_model=schemas.SongPagination)
def read_songs(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=0),
    db: Session = Depends(database.get_db),
):
    """
    Retrieve a list of songs with pagination.

    Args:
        skip (int): Number of records to skip (default is 0).
        limit (int): Maximum number of records to retrieve (default is 10).
        db (Session): SQLAlchemy database session dependency.

    Returns:
        schemas.SongPagination: Paginated list of songs including total count.

    Raises:
        HTTPException: If there's an issue retrieving songs.

    """
    total = db.query(models.Song).count()
    songs = db.query(models.Song).offset(skip).limit(limit).all()
    return schemas.SongPagination(total=total, skip=skip, limit=limit, data=songs)


@router.get("/{title}", response_model=schemas.Song)
def read_song(title: str, db: Session = Depends(database.get_db)):
    """
    Retrieve a song by its title (case-insensitive).

    Args:
        title (str): Title of the song to retrieve.
        db (Session): SQLAlchemy database session dependency.

    Returns:
        schemas.Song: Retrieved song.

    Raises:
        HTTPException: If the song with the given title is not found.

    """
    song = (
        db.query(models.Song)
        .filter(func.lower(models.Song.title) == func.lower(title))
        .first()
    )
    if song is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"song not found"
        )
    return song


@router.put("/{song_id}", response_model=schemas.Song)
def update_song(
    song_id: str, song: schemas.Song, db: Session = Depends(database.get_db)
):
    """
    Update a song by its ID.

    Args:
        song_id (str): ID of the song to update.
        song (schemas.Song): Updated song data.
        db (Session): SQLAlchemy database session dependency.

    Returns:
        schemas.Song: Updated song.

    Raises:
        HTTPException: If the song with the given ID is not found.

    """
    song = db.query(models.Song).filter(models.Song.id == song_id).first()
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    for var, value in vars(song).items():
        if value is not None:
            setattr(song, var, value)
    db.commit()
    db.refresh(song)
    return song

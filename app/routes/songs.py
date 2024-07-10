from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.engine import schemas, database, models

router = APIRouter(
    prefix="/songs",
    tags=["songs"]
)


@router.get("/", response_model=schemas.SongPagination)
def read_songs(skip: int = Query(0, ge=0), limit: int = Query(10, ge=0), db: Session = Depends(database.get_db)):
    total = db.query(models.Song).count()
    songs = db.query(models.Song).offset(skip).limit(limit).all()
    return schemas.SongPagination(total=total, skip=skip, limit=limit, data=songs)


@router.get("/{title}", response_model=schemas.Song)
def read_song(title: str, db: Session = Depends(database.get_db)):
    song = db.query(models.Song).filter(func.lower(models.Song.title) == func.lower(title)).first()
    if song is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"song not found")
    return song


@router.put("/{song_id}", response_model=schemas.Song)
def update_song(song_id: str, song: schemas.Song, db: Session = Depends(database.get_db)):
    song = db.query(models.Song).filter(models.Song.id == song_id).first()
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    for var, value in vars(song).items():
        if value is not None:
            setattr(song, var, value)
    db.commit()
    db.refresh(song)
    return song
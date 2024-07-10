from fastapi import APIRouter, Depends, Query
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

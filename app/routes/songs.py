from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.engine import schemas, database, models

router = APIRouter(
    prefix="/songs",
    tags=["songs"]
)


@router.get("/", response_model=list[schemas.Song])
def read_songs(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    songs = db.query(models.Song).offset(skip).limit(limit).all()
    return songs

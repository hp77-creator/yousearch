from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import crud, models, db
from models import VideoMetaData

router = APIRouter()


@router.get("/get-latest-videos")
def get_latest_videos(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    videos = crud.get_latest_videos(db, skip=skip, limit=limit)
    return videos

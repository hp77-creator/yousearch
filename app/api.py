from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import db
import task

router = APIRouter()


@router.get("/get-latest-videos")
def get_latest_videos(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    videos = crud.get_latest_videos(db, skip=skip, limit=limit)
    return videos


@router.get("/search/")
def search_keyword(title: str, description: str, skip: int = 0, limit: int = 10):
    videos = crud.search_with_keyword(title, description)
    return videos


@router.post("/trigger-celery-task")
async def trigger_celery_task():
    # Trigger Celery task using the delay method
    result = task.fetch_and_store_yt_data.delay()
    return {"message": "Celery task triggered", "task_id": result.id}

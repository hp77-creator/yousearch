from sqlalchemy.orm import Session
from sqlalchemy import desc
import models


def get_latest_videos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.VideoMetaData).order_by(desc(models.VideoMetaData.published_date)).offset(skip).limit(limit).all()

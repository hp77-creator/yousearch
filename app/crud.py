from sqlalchemy.orm import Session
from sqlalchemy import desc, create_engine, text
import models
from db import SQLALCHEMY_DB_URL


def get_latest_videos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.VideoMetaData).order_by(desc(models.VideoMetaData.published_date)).offset(skip).limit(
        limit).all()


def search_with_keyword(title: str, description: str):
    db = create_engine(SQLALCHEMY_DB_URL).connect()
    query = text("""
            SELECT * FROM videometadata 
            WHERE title LIKE :title AND description LIKE :description
        """).bindparams(title=f"%{title}%", description=f"%{description}%")
    result = db.execute(query)
    rows = result.fetchall()
    # above is coming as a list, fastapi expects dictionary
    keys = result.keys()

    data = [dict(zip(keys, row)) for row in rows]
    result.close()
    return data

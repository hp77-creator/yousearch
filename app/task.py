from celery import Celery
from celery.schedules import crontab
import os
from dotenv import load_dotenv
from app.db import SessionLocal
from youtube import fetch_yt_video
from constants import PREDEFINED_QUERY
from models import VideoMetaData

load_dotenv()

redis_url = os.environ.get("REDIS_URL", "redis://localhost:6379")
app = Celery(__name__, broker=redis_url, backend=redis_url)

app.conf.beat_schedule = {
    'fetch-and-store-task': {
        'task': f'{__name__}.fetch_and_store_yt_data',
        'schedule': crontab(minute="5")
    },
}

app.conf.timezone = 'UTC'


@app.task
def fetch_and_store_yt_data():
    db = SessionLocal()
    try:
        options = {
            "query": PREDEFINED_QUERY,
            "max_result": 3,
            "type": "video"
        }
        videos = fetch_yt_video(options)
        for video in videos:
            db_video = VideoMetaData(
                title=video['title'],
                description=video['description'],
                published_date=video['publishedAt'],
                thumbnail_url=video['thumbnail_url'],
                channel_url=video['channel_url'],
                channel_title=video['channel_title']
            )
            db.add(db_video)
        db.commit()
    finally:
        db.close()

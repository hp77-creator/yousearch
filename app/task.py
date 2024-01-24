import datetime
import random

from celery import Celery
from celery.schedules import crontab
import os
from dotenv import load_dotenv
from db import SessionLocal
from youtube import fetch_yt_video
from constants import PREDEFINED_QUERY, REFRESH_SECOND_TIME
from models import VideoMetaData
import logging

load_dotenv()

redis_url = os.environ.get("REDIS_URL", "redis://localhost:6379")
app = Celery(
    __name__,
    broker=redis_url,
    backend=redis_url,
    include=['task']
)

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch-and-store-task': {
        'task': f'{__name__}.fetch_and_store_yt_data',
        'schedule': crontab(minute="*/1")
    },
}

app.conf.timezone = 'UTC'


@app.task
def fetch_and_store_yt_data():
    logger = logging.getLogger(__name__)
    logger.info("Fetching and storing YouTube data...")
    db = SessionLocal()
    try:
        queries = ["NBA", "Football", "Cricket", "AI", "Programming", "news", "music", "movies", "vim"]
        random.seed(datetime.datetime.now().timestamp())
        search_query = queries[random.randint(0, len(queries)-1)]
        options = {
            "query": search_query,
            "max_result": 3,
            "type": "video"
        }
        videos = fetch_yt_video(options)
        logger.info("Videos fetched: %s", videos)
        print("videos fetched")
        for video in videos:
            print("current video: ", video)
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
    except Exception as e:
        logger.error("Error in fetch_and_store_yt_data: %s", str(e))
    finally:
        db.close()

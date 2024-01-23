import logging
import os

from googleapiclient import errors, discovery
from dotenv import load_dotenv
from googleapiclient.errors import HttpError

from .constants import YOUTUBE_WATCH_BASE_URL, YOUTUBE_CHANNEL_BASE_URL, PREDEFINED_QUERY

load_dotenv()

api_service_name = os.environ.get("SERVICE_NAME")
api_version = os.environ.get("VERSION")
developer_key = os.environ.get("API_KEY")

logger = logging.getLogger()


def parse_response(response, videos):
    required = [
        "title",
        "description",
        "publishedAt",
    ]
    for search_result in response.get('items', []):
        temp = dict()
        for req in required:
            temp[req] = search_result['snippet'][req]
        temp['thumbnail_url'] = search_result['snippet']['thumbnails']['default']['url']
        temp["video_url"] = "".join([YOUTUBE_WATCH_BASE_URL, search_result['id']['videoId']])
        temp["channel_url"] = "".join([YOUTUBE_CHANNEL_BASE_URL, search_result['snippet']['channelId']])
        temp["channel_title"] = search_result['snippet']['channelTitle']
        videos[search_result['id']['videoId']] = temp


def fetch_yt_video(query_options):
    try:
        youtube = discovery.build(
            api_service_name, api_version, developerKey=developer_key)
    except errors.UnknownApiNameOrVersion as e:
        logger.error("API Name or Version are not proper")
        exit(1)
    request = None
    try:
        request = youtube.search().list(
            part="id,snippet",
            q=query_options.get('query'),
            maxResults=query_options.get('max_result'),
            order='date',
            type=query_options.get('video')
        )
    except Exception as e:
        logger.error("Some error occurred " + str(e))
        exit(1)

    try:
        response = request.execute()
    except HttpError as e:
        logger.error("Error while doing request " + str(e))
        exit(1)

    videos = dict()
    parse_response(response, videos)
    print(videos)
    return videos


if __name__ == "__main__":
    import sys
    print(sys.path)
    options = {
        "query": PREDEFINED_QUERY,
        "max_result": 3,
        "type": "video"
    }
    fetch_yt_video(options)

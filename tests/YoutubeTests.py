import unittest

from app import youtube


class YoutubeTests(unittest.TestCase):

    def helper(self, response, options):
        self.assertTrue(response is not None, "response is none")
        self.assertEqual(len(response.keys()), options.get("max_result"), "lengths do not match")

    def test_fetch_yt_videos(self):
        options = {
            "query": "Cricket",
            "max_result": 4,
            "type": "video"
        }
        response = youtube.fetch_yt_video(options)
        print("videos are " + str(response))
        self.helper(response=response, options=options)

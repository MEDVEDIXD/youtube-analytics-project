import os
import json
from googleapiclient.discovery import build


class Video:
    def __init__(self, id_video):
        self.id_video = id_video
        self.__api_key = os.getenv('YouTubeAPI')
        youtube = build('youtube', 'v3', developerKey=self.__api_key)

        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=id_video
                                               ).execute()

        self.video_title = video_response['items'][0]['snippet']['title']
        self.video_url = f'https://www.youtube.com/watch?v={self.id_video}'
        self.video_view_count = video_response['items'][0]['statistics']['viewCount']
        self.video_likes_count = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.video_title}'


class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist
        self.__api_key = os.getenv('YouTubeAPI')
        youtube = build('youtube', 'v3', developerKey=self.__api_key)

        playlist_videos = youtube.playlistItems().list(playlistId=id_playlist,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

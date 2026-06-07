import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

youtube = build(
    "youtube",
    "v3",
    developerKey=os.getenv("YOUTUBE_API_KEY")
)


def get_channel_data(channel_name):
    search_response = youtube.search().list(
        q=channel_name,
        part="snippet",
        type="channel",
        maxResults=1
    ).execute()

    if not search_response["items"]:
        return None

    channel_id = (
        search_response["items"][0]
        ["snippet"]["channelId"]
    )

    channel_response = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    ).execute()

    if not channel_response["items"]:
        return None

    return channel_response["items"][0]
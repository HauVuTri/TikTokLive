import asyncio
import os

from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import ConnectEvent

client = TikTokLiveClient("@nuochoachinhhang12")


def get_unique_filename(filename, unique_id):
    i = 0
    new_filename = os.path.join(unique_id, filename)
    while os.path.exists(new_filename):
        i += 1
        new_filename = os.path.join(unique_id, f"{os.path.splitext(filename)[0]}-{i}{os.path.splitext(filename)[1]}")
    if not os.path.exists(unique_id):
        os.makedirs(unique_id)
    return new_filename


@client.on("connect")
async def on_connect(_: ConnectEvent):
    """
    Download the livestream video from TikTok directly!

    """
    cwd = os.getcwd()
    file_path = os.path.join(cwd, get_unique_filename('stream_today.mp4', client.unique_id))

    client.download(
        path=file_path,  # File path to save the download to
        duration=None,  # Download FOREVER. Set to any integer above 1 to download for X seconds
        quality=None  # Select video quality. In this case, Ultra-High Definition
    )

    # Stop downloading after 10 seconds.
    await asyncio.sleep(10)
    client.stop_download()


if __name__ == '__main__':
    """
    NOTE: You must have ffmpeg installed on your machine for this program to run!

    """

    client.run()

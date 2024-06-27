import requests
import re

video_url = ""
response = requests.get(video_url, stream=True)

with open(f"{video_name}第{id}集.mp4", "wb") as video_file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            video_file.write(chunk)

print("视频下载完成！")

from pathlib import Path
import yt_dlp
import csv

def download_video(url):
    # download one video
    Path("videos").mkdir(exist_ok=True)

    # Save inside videos/ using the video title as the filename
    ydl_options = {
        "outtmpl": "videos/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])

def read_video_urls(csv_path):
    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)

        return [row["url"] for row in reader]

        # for row in reader:
        #     print( row["url"])
            # print(row["title"], row["url"])

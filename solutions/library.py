from pathlib import Path
import yt_dlp
import csv

def download_video(url):
    # download one video
    Path("videos").mkdir(exist_ok=True)

    # Save inside videos/ using the video title as the filename
    ydl_options = {
        "outtmpl": "videos/%(title)s.%(ext)s",
        "socket_timeout": 30,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            ydl.download([url])

        return {
            "url": url,
            "status": "success",
            "error": "",
        }

    except Exception as error:
        return {
            "url": url,
            "status": "failed",
            "error": str(error),
        }

def read_video_urls(csv_path):
    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)

        return [row["url"] for row in reader]

        # for row in reader:
        #     print( row["url"])
            # print(row["title"], row["url"])

def get_video_metadata(url):
    ydl_options = {
    "quiet": True,
    "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        info = ydl.extract_info(url, download=False)

        metadata = {
            "title":info.get("title"),
            "duration": info.get("duration"),
            "uploader": info.get("uploader"),
            "view_count": info.get("view_count"),
            "ext": info.get("ext"),
            "url": url
        }
        print (metadata)
        return metadata


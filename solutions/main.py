import multiprocessing as mp

from library import *

def serial_execution():
    import time
    start = time.perf_counter()

    for video_url in read_video_urls("data/video_urls.csv"):
        print(f"Downloading {video_url}...")
        download_video(video_url)

    end = time.perf_counter()
    elapsed = end - start
    serial_time = round(elapsed, 2)
    print(f"Serial execution: {serial_time}")

def parellel_execution():
    import time
    start = time.perf_counter()
    url_list = read_video_urls("data/video_urls.csv")
    with mp.Pool(processes=5) as pool:
        results = pool.map(download_video, url_list)
    
    end = time.perf_counter()
    elapsed = end - start
    serial_time = round(elapsed, 2)
    print(f"Parallel execution: {serial_time}")


def save_metadata(urls):
    metadata_rows = []

    for url in urls:
        metadata = get_video_metadata(url)
        metadata_rows.append(metadata)
    print(metadata_rows)
    with open("data/video_metadata.csv", "w", newline="") as file:
        fieldnames = ["title", "duration", "uploader", "view_count", "ext", "url"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(metadata_rows)

def serial_execution_with_download_status():
    import time
    start = time.perf_counter()
    results = []

    for video_url in read_video_urls("data/video_urls.csv"):
        print(f"Downloading {video_url}...")
        status = download_video(video_url)
        results.append(status)
    
    print("Successful downloads:", len([result for result in results if result["status"] == "success"]))
    print("Failed  downloads:", len([result for result in results if result["status"] == "failed"]))

    for result in results:
        if result["status"] == "failed":
            print("Failed:", result["url"])
            print("Error:", result["error"])

    end = time.perf_counter()
    elapsed = end - start
    serial_time = round(elapsed, 2)
    print(f"Serial execution: {serial_time}")
    return results


if __name__ == "__main__":
    # Single download
    # download_video("https://www.youtube.com/watch?v=jNQXAC9IVRw")
    
    # Read from CSVs
    # read_video_urls("data/video_urls.csv")

    # serial_execution()
    # parellel_execution()

    # urls = read_video_urls("data/video_urls.csv")
    # save_metadata(urls)

    serial_execution_with_download_status()
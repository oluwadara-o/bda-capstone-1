import multiprocessing as mp

from library import download_video, read_video_urls

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

if __name__ == "__main__":
    parellel_execution()
    # serial_execution()
    # read_video_urls("data/video_urls.csv")
    # print("done1")
    # download_video("https://www.youtube.com/watch?v=jNQXAC9IVRw")

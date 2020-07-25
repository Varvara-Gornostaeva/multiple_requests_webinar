from datetime import datetime
import requests
import concurrent.futures
import time


url = 'http://localhost:8000/'


def get_result(num):
    response = requests.get(url=url, params={'num': num})
    return response.text


time_start = datetime.now()
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    futures = []
    for _ in range(1):
        futures.append(executor.submit(get_result, 100000))

    for future in concurrent.futures.as_completed(futures):
        print(future.result())


time_end = datetime.now()
elapsed_time = time_end - time_start
print(f'All calculated {elapsed_time}')

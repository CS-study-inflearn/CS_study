import time
import threading
import requests
from concurrent.futures import ThreadPoolExecutor

# CPU 바운드 작업
def cpu_bound_task(n):
    return sum(i*i for i in range(n))

# I/O 바운드 작업
def io_bound_task(url):
    response = requests.get(url)
    return response.status_code

# 싱글 스레딩 실행 함수
def run_single_threaded(tasks, task_type):
    start_time = time.time()
    results = []
    for task in tasks:
        results.append(task_type(task))
    end_time = time.time()
    print(f"싱글 스레딩 결과: {len(results)}개, 시간: {end_time - start_time:.2f}초")

# 멀티 스레딩 실행 함수
def run_multi_threaded(tasks, task_type):
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(task_type, tasks))
    end_time = time.time()
    print(f"멀티 스레딩 결과: {len(results)}개, 시간: {end_time - start_time:.2f}초")

if __name__ == "__main__":
    n = 10**7
    urls = ["https://www.example.com" for _ in range(4)]  # 동일한 URL로 4개의 요청

    print("CPU 바운드 작업 (싱글 스레딩 vs 멀티 스레딩)")
    run_single_threaded([n] * 4, cpu_bound_task)
    run_multi_threaded([n] * 4, cpu_bound_task)

    print("\nI/O 바운드 작업 (싱글 스레딩 vs 멀티 스레딩)")
    run_single_threaded(urls, io_bound_task)
    run_multi_threaded(urls, io_bound_task)

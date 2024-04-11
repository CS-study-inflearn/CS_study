# -*- coding: utf-8 -*-

from java.util.concurrent import Executors, TimeUnit
from java.net import URL
from java.lang import Runnable
from java.lang import System as JavaSystem

# CPU 바운드 작업
class SumTask(Runnable):
    def __init__(self, n):
        self.n = n
    
    def run(self):
        total = sum(i for i in range(self.n))
        print("Sum:", total)

# I/O 바운드 작업
class DownloadTask(Runnable):
    def __init__(self, url):
        self.url = url
    
    def run(self):
        content = URL(self.url).openStream()
        content.close()
        print("Download completed")

# 작업 실행 함수
def execute_tasks_single_threaded(tasks):
    start_time = JavaSystem.currentTimeMillis()
    for task in tasks:
        task.run()
    end_time = JavaSystem.currentTimeMillis()
    print("Single Thread:", (end_time - start_time), "ms")

def execute_tasks_multi_threaded(tasks):
    executor = Executors.newFixedThreadPool(4)
    start_time = JavaSystem.currentTimeMillis()
    for task in tasks:
        executor.submit(task)
    executor.shutdown()
    executor.awaitTermination(60, TimeUnit.SECONDS)
    end_time = JavaSystem.currentTimeMillis()
    print("Multi Thread:", (end_time - start_time), "ms")

if __name__ == '__main__':
    # CPU 바운드 작업 비교
    print("CPU Bound")
    n = 10000000
    cpu_tasks = [SumTask(n) for _ in range(4)]
    execute_tasks_single_threaded(cpu_tasks)
    execute_tasks_multi_threaded(cpu_tasks)

    # I/O 바운드 작업 비교
    print("\nI/O Bound")
    urls = ["http://www.example.com" for _ in range(4)]
    io_tasks = [DownloadTask(url) for url in urls]
    execute_tasks_single_threaded(io_tasks)
    execute_tasks_multi_threaded(io_tasks)

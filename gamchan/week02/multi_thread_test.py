import threading
import time

# CPU 바운드 작업을 수행하는 함수
def cpu_bound_task(n):
    return sum(i*i for i in range(n))

def single_threaded(n):
    start_time = time.time()
    results = []
    for _ in range(n):
        result = cpu_bound_task(10**7)
        results.append(result)
    end_time = time.time()
    print(f"싱글 스레딩 결과: {sum(results)}, 시간: {end_time - start_time}초")

def multi_threaded(n):
    threads = []
    results = [0] * n
    start_time = time.time()
    
    for i in range(n):
        # 각 스레드에 작업 분배
        thread = threading.Thread(target=lambda q, idx: q.__setitem__(idx, cpu_bound_task(10**7)), args=(results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # 모든 스레드의 작업이 끝날 때까지 기다림
    
    end_time = time.time()
    print(f"멀티 스레딩 결과: {sum(results)}, 시간: {end_time - start_time}초")

if __name__ == "__main__":
    print("싱글 스레딩 실행 중...")
    single_threaded(4)  # 4번 반복 실행
    
    print("\n멀티 스레딩 실행 중...")
    multi_threaded(4)  # 4개의 스레드 생성

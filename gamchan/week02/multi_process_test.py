import time
from multiprocessing import Process, cpu_count

# 팩토리얼 계산 함수
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 멀티 프로세스에서 실행할 타겟 함수
def compute_factorials():
    factorial(100000)

def single_process():
    # 단일 프로세스 실행 시간 측정
    start_time = time.time()
    results = [factorial(100000) for _ in range(2)]  # 큰 숫자의 팩토리얼을 두 번 계산
    end_time = time.time()
    print(f"Single Process Time: {end_time - start_time} seconds")

def multi_process():
    # 멀티 프로세스 실행 시간 측정
    start_time = time.time()
    
    processes = []
    num_processes = 2  # 동시에 실행할 프로세스의 수
    for _ in range(num_processes):
        p = Process(target=compute_factorials)
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()  # 모든 프로세스의 종료를 기다림
    
    end_time = time.time()
    print(f"Multi Process Time: {end_time - start_time} seconds")

if __name__ == '__main__':
    single_process()  # 단일 프로세스로 실행
    multi_process()   # 멀티 프로세스로 실행

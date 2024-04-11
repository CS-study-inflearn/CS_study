from multiprocessing import Process, Value, Lock, Semaphore

def increment_without_sync(shared_counter):
    for _ in range(100000):
        shared_counter.value += 1

def increment_with_lock(shared_counter, lock):
    for _ in range(100000):
        with lock:
            shared_counter.value += 1

def increment_with_semaphore(shared_counter, semaphore):
    for _ in range(100000):
        with semaphore:
            shared_counter.value += 1

if __name__ == '__main__':
    # 동기화 없이
    counter = Value('i', 0)
    p1 = Process(target=increment_without_sync, args=(counter,))
    p2 = Process(target=increment_without_sync, args=(counter,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Final counter value without synchronization: {counter.value}")

    # 뮤텍스(Lock)를 사용하여
    counter.value = 0  # 카운터 초기화
    lock = Lock()
    p1 = Process(target=increment_with_lock, args=(counter, lock))
    p2 = Process(target=increment_with_lock, args=(counter, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Final counter value with mutex (Lock): {counter.value}")

    # 세마포어를 사용하여
    counter.value = 0  # 카운터 초기화
    semaphore = Semaphore(2)  # 동시에 최대 2개의 프로세스만 접근 허용
    p1 = Process(target=increment_with_semaphore, args=(counter, semaphore))
    p2 = Process(target=increment_with_semaphore, args=(counter, semaphore))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Final counter value with semaphore: {counter.value}")

from multiprocessing import Process, Value

def increment(shared_value):
    for _ in range(10000):
        shared_value.value += 1

if __name__ == "__main__":
    shared_value = Value('i', 0)  # 공유 메모리 생성
    p1 = Process(target=increment, args=(shared_value,))
    p2 = Process(target=increment, args=(shared_value,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Final value: {shared_value.value}")

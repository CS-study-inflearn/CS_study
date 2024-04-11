from multiprocessing import Process, Value
import ctypes


def increment(shared_counter):
    for _ in range(100000):
        shared_counter.value += 1

if __name__ == '__main__':
    # 공유 메모리 값 생성
    counter = Value('i', 0)

    # 프로세스 생성
    process1 = Process(target=increment, args=(counter,))
    process2 = Process(target=increment, args=(counter,))

    # 프로세스 시작
    process1.start()
    process2.start()

    # 프로세스가 끝나길 기다림
    process1.join()
    process2.join()

    print(f"Expected counter value: 200000, Actual counter value: {counter.value}")

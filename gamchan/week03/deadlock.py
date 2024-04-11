import threading
import time

# 두 개의 자원을 위한 락 생성
lock1 = threading.Lock()
lock2 = threading.Lock()

# 스레드 1의 작업
def thread1_work():
    while True:
        with lock1:
            print("Thread 1 has acquired lock1")
            time.sleep(1)
            with lock2:
                print("Thread 1 has acquired lock2")
        print("Thread 1 is done")

# 스레드 2의 작업
def thread2_work():
    while True:
        with lock2:
            print("Thread 2 has acquired lock2")
            time.sleep(1)
            with lock1:
                print("Thread 2 has acquired lock1")
        print("Thread 2 is done")

# 스레드 생성 및 시작
t1 = threading.Thread(target=thread1_work)
t2 = threading.Thread(target=thread2_work)

t1.start()
t2.start()

t1.join()
t2.join()

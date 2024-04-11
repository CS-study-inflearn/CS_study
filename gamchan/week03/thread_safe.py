import threading
import time

# 상호 배제를 위한 락 객체
lock = threading.Lock()

# 원자 연산 예제로, 간단한 플래그 변수 사용
operation_done = False

# 스레드 지역 저장소 생성
thread_local = threading.local()

# 재진입 가능한 함수
def reentrant_function():
    # 스레드 지역 저장소에 값 설정. 각 스레드는 자신만의 unique_value를 가짐
    if not hasattr(thread_local, "unique_value"):
        thread_local.unique_value = 0

    # 상호 배제를 보장하기 위해 락을 사용
    with lock:
        # 원자 연산 사용 (여기서는 간단한 플래그 체크)
        global operation_done
        if not operation_done:
            print(f"Performing an operation in {threading.current_thread().name}")
            thread_local.unique_value += 1  # 스레드 지역 저장소 사용
            operation_done = True  # 원자 연산으로 상태 변경
        else:
            print(f"Operation was already performed by another thread")

    # 재진입성을 보여주기 위한 출력. 동일한 함수가 다른 스레드에서 실행되어도, 각 스레드는 올바른 결과를 가짐
    print(f"{threading.current_thread().name}'s unique value: {thread_local.unique_value}")

# 스레드를 생성하고 시작하는 함수
def start_thread():
    for i in range(2):
        t = threading.Thread(target=reentrant_function, name=f"Thread-{i+1}")
        t.start()
        time.sleep(1)  # 스레드 실행 간격

start_thread()

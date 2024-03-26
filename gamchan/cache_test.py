import numpy as np
import time

n = 10000
data = np.random.rand(n, n) # n x n 배열 생성

start_time = time.time()
row_sum = 0
for i in range(n):
    for j in range(n):
        row_sum += data[i][j] # 행 우선 접근
row_access_time = time.time() - start_time

start_time = time.time()
col_sum = 0
for i in range(n):
    for j in range(n):
        col_sum += data[j][i] # 열 우선 접근
col_access_time = time.time() - start_time

print(f"row_sum: {row_sum}, 행 우선 접근 시간: {row_access_time}초")
print(f"col_sum: {col_sum}, 열 우선 접근 시간: {col_access_time}초")
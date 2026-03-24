import sys
input = sys.stdin.readline
import math

n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

for i in range(n) :
    strings = input().strip()
    for j in range(m) :
        arr[i][j] = int(strings[j])

dp = [[0] * m for _ in range(n)]

max_val = 0

# 첫 줄 처리
dp[0][0] = arr[0][0]
max_val = max(arr[0][0], max_val)

for i in range(1, n) :
    dp[i][0] = arr[i][0]
    max_val = max(arr[i][0], max_val)

for j in range(1, m) :
    dp[0][j] = arr[0][j]
    max_val = max(arr[0][j], max_val)

# dp
for i in range(1, n) :
    for j in range(1, m) :
        if arr[i][j] == 1 :
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            max_val = max(max_val, dp[i][j])

print(max_val * max_val)
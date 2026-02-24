import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
max_dp = arr
min_dp = arr

for _ in range(1, n) :
    arr = list(map(int, input().split()))

    max_temp = [0] * 3
    min_temp = [0] * 3

    max_temp[0] = max(max_dp[0], max_dp[1]) + arr[0]
    min_temp[0] = min(min_dp[0], min_dp[1]) + arr[0]

    max_temp[1] = max(max_dp[0], max_dp[1], max_dp[2]) + arr[1]
    min_temp[1] = min(min_dp[0], min_dp[1], min_dp[2]) + arr[1]

    max_temp[2] = max(max_dp[1], max_dp[2]) + arr[2]
    min_temp[2] = min(min_dp[1], min_dp[2]) + arr[2]

    max_dp = max_temp
    min_dp = min_temp

print(max(max_dp), min(min_dp))

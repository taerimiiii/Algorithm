import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())

dp = [1] * (n+1)
for _ in range(b) :
    breaking = int(input())
    dp[breaking] = 0
dp[0] = 0

for i in range(2, n+1) :
    dp[i] += dp[i-1]

min_val = 100000
for i in range(n-k+1) :
    min_val = min(min_val, k - (dp[i+k] - dp[i]))

print(min_val)
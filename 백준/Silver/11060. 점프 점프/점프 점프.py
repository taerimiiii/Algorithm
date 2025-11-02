import sys
input = sys.stdin.readline

def in_range(x) :
    if 0 <= x < n :
        return True
    return False

n = int(input())
arr = list(map(int, input().split()))

dp = [1001] * n
dp[0] = 0
for i in range(n) :
    for j in range(1, arr[i]+1) :
        if in_range(i+j) :
            dp[i+j] = min(dp[i] + 1, dp[i+j])

if dp[-1] == 1001 :
    print(-1)
else :
    print(dp[-1])
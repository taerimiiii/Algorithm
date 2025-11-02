import sys
input = sys.stdin.readline

n = int(input())
dp = [i for i in range(n+1)]

for i in range(2, n+1) :
    for j in range(1, i+1) :
        sq = j * j
        if sq > i :
            break
        
        if dp[i] > dp[i-sq] + 1 :
            dp[i] = dp[i-sq] + 1

print(dp[n])
def get_tile(idx) :
    dp[idx] = dp[idx - 1] + dp[idx - 2]
    return dp[idx]

n = int(input())
dp = [0] * (n + 1)

i = 0
while i < n + 1 :
    if i == 0 or i == 1 :
        dp[i] = 1
    else :
        get_tile(i)
    i += 1

print(dp[n] % 10007)
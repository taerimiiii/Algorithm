def get_fib(idx) :
    dp[idx] = (dp[idx - 1] + dp[idx - 2]) % 1000000007
    return dp[idx]

n = int(input())
dp = [0] * (n + 1)

i = 0
while i < n + 1 :
    if i == 0 :
        dp[i] = 0
    elif i == 1 :
        dp[i] = 1
    else :
        dp[i] = get_fib(i)
    i += 1

print(dp[n])
def get_calculate(idx) :
    cal1, cal2 = 50000, 50000
    if idx % 3 == 0 :
        cal1 = dp[idx // 3] + 1
    if idx % 2 == 0 :
        cal2 = dp[idx // 2] + 1
    dp[idx] = min(cal1, cal2, dp[idx - 1] + 1)
    return dp[idx]

n = int(input())
dp = [0] * (n + 1)

i = 2
while i < n + 1 :
    if i == 2 or i == 3 :
        dp[i] = 1
    else :
        get_calculate(i)
    i += 1

print(dp[n])
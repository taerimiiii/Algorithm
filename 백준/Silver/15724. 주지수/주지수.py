n, m = map(int, input().split())
arr_2d = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
scope = [list(map(int, input().split())) for _ in range(k)]

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = arr_2d[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for i in range(k):
    x1, y1, x2, y2 = scope[i]
    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# dp[r][c][0]: 가로, dp[r][c][1]: 대각선, dp[r][c][2]: 세로
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

# 시작 위치
dp[0][1][0] = 1

# 첫 번째 행 가로로만 이동
for i in range(2, n) :
    if arr[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]

# dp
for r in range(1, n) :
    for c in range(1, n) :
        # 대각선
        if arr[r][c] == 0 and arr[r][c-1] == 0 and arr[r-1][c] == 0 :
            dp[r][c][1] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]
        
        # 가로 세로
        if arr[r][c] == 0 :
            # 가로 or 대각선 -> 가로
            dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][1]
            # 세로 or 대각선 -> 세로
            dp[r][c][2] = dp[r-1][c][2] + dp[r-1][c][1]

print(sum(dp[n-1][n-1]))
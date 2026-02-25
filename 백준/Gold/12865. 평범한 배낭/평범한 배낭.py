import sys
input = sys.stdin.readline

# 2차원 dp 풀이

n, k = map(int, input().split())
weight = [0] * (n+1)
value = [0] * (n+1)
for i in range(1, n+1) :
    weight[i], value[i] = map(int, input().split())

dp = [[0] * (k+1) for _ in range(n+1)]  # 행: 물건의 갯수 (0 ~ n) / 열: 가방의 최대용량(0 ~ k)
for target in range(1, n+1) :           # target: 모든 물건을 순차적으로 탐색
    for idx in range(1, k+1) :          # idx: 가방의 최대용량을 1부터 k까지 증가
        if idx >= weight[target] :      # 물건을 가방에 넣을 수 있다면
            dp[target][idx] = max(dp[target-1][idx], # 이전 물건까지 넣은 케이스와, 이전 물건에서 지금 물건을 넣을 무게만큼
                                  dp[target-1][idx-weight[target]] + value[target]) # 딱 뺀 경우에 지금 물건을 더한 것 중 큰걸 저장.
        else:                           # 물건을 가방에 넣지 못한다면
            dp[target][idx] = dp[target-1][idx]   # 이전 물건까지 넣은 케이스를 받는다. (이전 물건까지 넣은 케이스가 최대이므로)

print(dp[-1][-1])
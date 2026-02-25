import sys
input = sys.stdin.readline

# 1차원 dp 풀이

n, k = map(int, input().split())
weight = [0] * (n+1)
value = [0] * (n+1)
for i in range(1, n+1) :
    weight[i], value[i] = map(int, input().split())

dp = [0] * (k+1)                    # 가방의 최대용량(0 ~ k)
for target in range(1, n+1) :       # target: 모든 물건을 순차적으로 탐색
    for idx in range(k, 0, -1) :    # idx: 가방의 최대용량을 k부터 1까지 역으로 탐색
        if idx >= weight[target] :  # 물건을 가방에 넣을 수 있다면
            dp[idx] = max(dp[idx],  # 원래 가방에 넣을 수 있던 값과, 물건의 무게만큼 뺀 경우 dp 값에 지금 넣을 물건 값을
                          dp[idx-weight[target]] + value[target]) # 더한 것 중 큰걸 저장

print(dp[-1])
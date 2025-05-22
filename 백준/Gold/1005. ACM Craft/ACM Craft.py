from collections import deque
from sys import stdin
input = stdin.readline

t = int(input())
res = []

for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [ [] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    dp = [0] * (n + 1)
    for _ in range(k):
        a, b = map(int ,input().split())
        graph[a].append(b)
        indegree[b] += 1

    que = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            que.append(i)
            dp[i] = time[i]

    while que:
        tmp = que.popleft()
        for i in graph[tmp]:
            indegree[i] -= 1 
            dp[i] = max(dp[tmp] + time[i], dp[i])
            if indegree[i] == 0:
                que.append(i)

    w = int(input())
    res.append(dp[w])

for i in res:
    print(i)

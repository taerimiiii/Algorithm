import sys
input = sys.stdin.readline
from heapq import heappop, heappush


INF = 10001
dists, res = [], []


def dijkstra(start: int, n: int) -> None:
    global dists, res

    hq = []
    for i in range(1, n + 1):
        if i == start:
            continue
        heappush(hq, (dists[start][i], i))

    while hq:
        dist, node = heappop(hq)

        if dists[start][node] < dist:
            continue
        for neighbor in range(1, n + 1):
            if node == neighbor or start == neighbor:
                continue
            if dist + dists[node][neighbor] < dists[start][neighbor]:
                dists[start][neighbor] = dist + dists[node][neighbor]
                heappush(hq, (dist + dists[node][neighbor], neighbor))
                res[start][neighbor] = res[start][node]



n, m = map(int, input().split())
dists = list(([INF] * (n + 1)) for _ in range(n + 1))
res = [['-'] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    dists[a][b] = dists[b][a] = w
    res[a][b] = str(b)
    res[b][a] = str(a)

for i in range(1, n + 1):
    dijkstra(i, n)

for line in res[1:]:
    print(*line[1:], sep=' ')

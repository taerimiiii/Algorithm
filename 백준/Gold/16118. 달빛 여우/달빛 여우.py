import sys
input = sys.stdin.readline
from heapq import *

n, m = map(int,input().split())

graph = [[] for i in range(n)]
for _ in range(m):
  a, b, c = map(int,input().split())
  graph[a - 1].append((b - 1,c * 2))
  graph[b - 1].append((a - 1,c * 2))

fox = [1e12] * n
hq = [(0 , 0)]
while hq:
  w, now = heappop(hq)
  if fox[now] < w:
    continue
  for next, w1 in graph[now]:
    if fox[next] > w + w1:
      fox[next] = w + w1
      heappush(hq,(w + w1,next))

wolf = [[1e12] * n for i in range(2)]
hq = [(0, 0, 0)]
while hq:
  w, now, s = heappop(hq)
  if wolf[s][now] < w:
    continue
  for next, w1 in graph[now]:
    if s:
      w1 <<= 1
    else:
      w1 >>= 1
    if wolf[s ^ 1][next] > w + w1:
      wolf[s ^ 1][next] = w + w1
      heappush(hq,(w + w1, next, s ^ 1))

print(sum( [int(fox[i] < min(wolf[0][i], wolf[1][i]) ) for i in range(1, n)]))

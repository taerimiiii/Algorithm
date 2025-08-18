import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, start) :
  visited = [False] * (n+1)
  queue = deque()
  queue.append(start)
  visited[start] = True

  while queue :
    node = queue.popleft()
    for neighbor in graph[node] :
      if not visited[neighbor] :
        queue.append(neighbor)
        visited[neighbor] = True

  cnt = 0
  for elem in visited :
    if elem :
      cnt += 1
  return cnt
        
n = int(input())
v = int(input())

graph = {i: [] for i in range(1, n+1)}
for _ in range(v) :
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

print(bfs(graph, 1)-1)
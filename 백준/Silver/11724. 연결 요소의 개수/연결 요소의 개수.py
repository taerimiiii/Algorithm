import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, graph, visited) :
  queue = deque()
  queue.append(start)
  visited[start] = True
  
  while queue :
    node = queue.popleft()
    for neighbor in graph[node] :
      if not visited[neighbor] :
        queue.append(neighbor)
        visited[neighbor] = True

  return visited


n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
visited = [False] * (n+1)
for _ in range(m) :
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

answer = 0
visited[0] = True
for i in range(n+1) :
  if not visited[i] :
    answer += 1
    visited = bfs(i, graph, visited)

print(answer)
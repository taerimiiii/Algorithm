import sys
input = sys.stdin.readline
from collections import deque

def dfs(graph, visited, start) :
  visited[start] = True
  print(start, end = ' ')

  for neighbor in graph[start] :
    if not visited[neighbor] :
      dfs(graph, visited, neighbor)


def bfs(graph, start) :
  queue = deque()
  queue.append(start)
  visited = [False] * (n+1)
  visited[start] = True

  while queue :
    node = queue.popleft()
    print(node, end = ' ')
    for neighbor in graph[node] :
      if not visited[neighbor] :
        queue.append(neighbor)
        visited[neighbor] = True

n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m) :
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, n+1) :
  graph[i].sort()

visited = [False] * (n+1)
dfs(graph, visited, v)
print()

bfs(graph, v)
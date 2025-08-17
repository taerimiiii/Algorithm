import sys
input = sys.stdin.readline
from collections import deque

def dfs(stack, cnt) :
  while stack :
    node = stack.pop()
    if not visited[node] :
      visited[node] = True
      turns[node] = cnt
      cnt += 1

      for neighbor in graph[node] :
        if not visited[neighbor] :
          stack.append(neighbor)
    
    #dfs(stack, cnt)

n, m, r = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
visited = [False] * (n+1)
stack = deque()
turns = [0] * (n+1)
cnt = 1

for _ in range(m) :
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

for key in graph :
  graph[key].sort()

stack.append(r)
dfs(stack, cnt)

for i in range(1, n+1) :
  print(turns[i])
import sys
input = sys.stdin.readline
from collections import deque

def in_range(x, y) :
  if 0 <= x < n and 0 <= y < m :
    return True
  return False

def bfs(graph, start_x, start_y) :
  queue = deque()
  queue.append((start_x, start_y))
  graph[start_x][start_y] = 0
  dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

  while queue :
    x, y = queue.popleft()
    for direct in range(4) :
      nx, ny = x + dxs[direct], y + dys[direct]
      if not in_range(nx, ny) :
        continue
      if graph[nx][ny] :
        queue.append((nx, ny))
        graph[nx][ny] = 0
  
  return graph

t = int(input())
for _ in range(t) :
  m, n, k = map(int, input().split())
  arr = [ [0] * m for _ in range(n) ]
  answer = 0
  for _ in range(k) : 
    y, x = map(int, input().split())
    arr[x][y] = 1
  for i in range(n) :
    for j in range(m) :
      if arr[i][j] :
        arr = bfs(arr, i, j)
        answer += 1
  print(answer)
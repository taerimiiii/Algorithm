import sys
input = sys.stdin.readline
from collections import deque

def in_range(x, y) :
  if 0 <= x < n and 0 <= y < m :
    return True
  return False

def bfs(arr, visited, start_x, start_y) :
  queue = deque()
  visited[start_x][start_y] = True
  queue.append(start_x)
  queue.append(start_y)

  area = 1
  dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

  while queue :
    x = queue.popleft()
    y = queue.popleft()
    for direct in range(4) :
      nx, ny = x + dxs[direct], y + dys[direct]
      if not in_range(nx, ny) :
        continue
      if not visited[nx][ny] and arr[nx][ny] :
        queue.append(nx)
        queue.append(ny)
        area += 1
        visited[nx][ny] = True

  return area


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

picture_cnt = 0
picture_area = 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(n) :
  for j in range(m) :
    if arr[i][j] == 1 and not visited[i][j] :
      area = bfs(arr, visited, i, j)
      picture_area = max(picture_area, area)
      picture_cnt += 1

print(picture_cnt)
print(picture_area)
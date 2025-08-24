import sys
input = sys.stdin.readline
from collections import deque

# 격자 내 범위인지 확인하는 함수
def in_range(x, y) :
  if 0 <= x < n and 0 <= y < m :
    return True
  return False

# 너비 우선 탐색
def bfs(arr, visited, start_x, start_y) :
  queue = deque()

  # 큐에 시작 지점 넣고, 방문 처리
  queue.append((start_x, start_y))
  visited[start_x][start_y] = True

  area = 1           # 넓이 초기값. 이미 시작 지점이므로 0이 아닌 1
  dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 순서대로 우하좌상 방향

  while queue :         # 큐가 비어있지 않을 동안
    x, y = queue.popleft() # 큐에 들어있는 x, y 좌표 pop
    for direct in range(4) : # x, y 좌표를 기준으로 상하좌우 네 방향 탐색
      nx, ny = x + dxs[direct], y + dys[direct]
      if not in_range(nx, ny) : # 격자 범위 내에 없다면 건너뛰기
        continue
      if arr[nx][ny] and not visited[nx][ny] : # 격자가 색칠되고, 격자를 방문한 적이 없다면 (=연결됨)
        queue.append((nx, ny))                       # 큐에 탐색한 x, y 좌표를 삽입
        area += 1                              # 넓이 + 1 (연결되었으므로)
        visited[nx][ny] = True                 # 연결된 좌표 방문 처리

  return area  # 한 그림 덩어리의 넓이 리턴

# 입력 처리
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
picture_cnt = 0     # 그림의 개수
picture_area = 0    # 가장 넓은 그림

for i in range(n) :   # 모든 격자 내부를 돌며
  for j in range(m) :
    if arr[i][j] and not visited[i][j] : # 격자가 색칠(1)되고, 격자를 방문한 적이 없으면 (=new 그림)
      picture_cnt += 1                        # 그림 개수 + 1 (새로운 그림 이므로)
      area = bfs(arr, visited, i, j)          # 그림의 넓이 구하기(bfs)
      picture_area = max(picture_area, area)  # 최대 그림 넓이로 갱신

# 출력 처리
print(picture_cnt)
print(picture_area)
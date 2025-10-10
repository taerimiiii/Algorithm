import sys
input = sys.stdin.readline
from collections import deque

def in_range(x, y, z) :
    if 0 <= x < h and 0 <= y < n and 0 <= z < m :
        return True
    return False

m, n, h = map(int, input().split())
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

queue = deque()
not_grow = 0

for i in range(h) :
    for j in range(n) :
        li = list(map(int, input().split()))
        for k in range(m) :
            if li[k] == 1 :
                queue.append([i, j, k])
                visited[i][j][k] = True
            elif li[k] == -1 :
                visited[i][j][k] = True
            else :
                not_grow += 1

dxs, dys, dzs = [1, -1, 0, 0, 0, 0], [0, 0, 0, 0, 1, -1], [0, 0, -1, 1, 0, 0] # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
is_grow = 0
total_cnt = 0

while queue :
    length = len(queue)
    for _ in range(length) :
        x, y, z = queue.popleft()
        for direct in range(6) :
            nx, ny, nz = x + dxs[direct], y + dys[direct], z + dzs[direct]
            if in_range(nx, ny, nz) and not visited[nx][ny][nz] :
                queue.append([nx, ny, nz])
                visited[nx][ny][nz] = True
                is_grow += 1
    total_cnt += 1
            
if not_grow != is_grow :
    print(-1)
else :
    print(total_cnt - 1) # while문의 맨 마지막 반복은 아무것도 큐에 추가되지 않는 경우이므로, -1 해준다.
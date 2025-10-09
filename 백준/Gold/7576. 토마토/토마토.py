import sys
input = sys.stdin.readline
from collections import deque

def in_range(x, y) :
    if 0 <= x < n and 0 <= y < m :
        return True
    return False

m, n = map(int, input().split())
visited = [[False] * m for _ in range(n)]

queue = deque()
not_grow = 0

for i in range(n) :
    li = list(map(int, input().split()))
    for j in range(m) :
        if li[j] == 1 :
            queue.append([i, j])
            visited[i][j] = True
        elif li[j] == -1 :
            visited[i][j] = True
        else :
            not_grow += 1

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
is_grow = 0
total_cnt = 0

while queue :
    length = len(queue)
    for _ in range(length) :
        x, y = queue.popleft()
        for direct in range(4) :
            nx, ny = x + dxs[direct], y + dys[direct]
            if in_range(nx, ny) and not visited[nx][ny] :
                queue.append([nx, ny])
                visited[nx][ny] = True
                is_grow += 1
    total_cnt += 1
            
if not_grow != is_grow :
    print(-1)
else :
    print(total_cnt - 1) # while문의 맨 마지막 반복은 아무것도 큐에 추가되지 않는 경우이므로, -1 해준다.
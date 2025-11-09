import sys
input = sys.stdin.readline
from collections import deque

def in_range(x, y) :
    if 0 <= x < n and 0 <= y < m :
        return True
    return False

def bfs(start_x, start_y, is_baby, arr) :
    queue = deque()
    queue.append((start_x, start_y))
    dxs, dys = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

    while queue :
        x, y = queue.popleft()
        for direct in range(8) :
            nx, ny = x + dxs[direct], y + dys[direct]
            if in_range(nx, ny) and not is_baby[nx][ny] :
                if arr[nx][ny] == 0 :
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx, ny))
                else :
                    if arr[x][y] + 1 < arr[nx][ny] :
                        arr[nx][ny] = arr[x][y] + 1
                        queue.append((nx, ny))

    return arr

# 입력 처리
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 아기 상어 위치 찾기
babies = []
is_baby = [[False] * m for _ in range(n)]
for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 1 :
            babies.append((i, j))
            is_baby[i][j] = True
            arr[i][j] = 0

# 최소 거리 구하기
length = len(babies)
for i in range(length) :
    x, y = babies[i]
    arr = bfs(x, y, is_baby, arr)

max_val = 0
for i in range(n) :
    for j in range(m) :
        max_val = max(max_val, arr[i][j])
    #     print(arr[i][j], end=' ')
    # print()

print(max_val)

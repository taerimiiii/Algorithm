from collections import deque

def bfs(x, y) :
    queue = deque()
    queue.append([x, y])
    arr[x][y] = 0

    while queue :
        x, y = queue.popleft()
        for i in range(8) :
            nx, ny = x + dx[i], y + dy[i]

            if in_range(nx, ny) :
                if arr[nx][ny] == 1 :
                    queue.append([nx, ny])
                    arr[nx][ny] = 0

def in_range(x, y) :
    global w, h
    if 0 <= x < h and 0<= y < w :
        return 1
    return 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

while 1 :
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    for i in range(h) :
        for j in range(w) :
            if arr[i][j] == 1 :
                bfs(i, j)
                cnt += 1
    print(cnt)

    

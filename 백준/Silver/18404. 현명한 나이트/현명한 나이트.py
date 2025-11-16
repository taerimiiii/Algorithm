import sys
input = sys.stdin.readline
from collections import deque

def in_range(x, y) :
    if 0 <= x < n and 0 <= y < n :
        return True
    return False

def bfs(x, y, target_map, visited, m) :
    queue = deque()
    queue.append([x, y])
    dxs, dys = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]
    loop_cnt = 0
    get_target_cnt = 0

    while get_target_cnt != m :
        length = len(queue)
        loop_cnt += 1

        for _ in range(length) :
            x, y = queue.popleft()

            for direct in range(8) :
                nx, ny = x + dxs[direct], y + dys[direct]
                
                if in_range(nx, ny) and not visited[nx][ny] :
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    
                    if target_map[nx][ny] == 1 :
                        get_target_cnt += 1
                        target_map[nx][ny] = loop_cnt

    return target_map


n, m = map(int, input().split())
x, y = map(int, input().split())
targets = [ list(map(int, input().split())) for _ in range(m) ]

target_map = [ [0] * n for _ in range(n) ]
for i in range(m) :
    a, b = targets[i]
    target_map[a-1][b-1] = 1

visited = [ [False] * n for _ in range(n) ]
visited[x-1][y-1] = True

target_map = bfs(x-1, y-1, target_map, visited, m)

for i in range(m) :
    a, b = targets[i]
    print(target_map[a-1][b-1], end=' ')
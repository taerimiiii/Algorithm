import sys
input = sys.stdin.readline
from collections import deque

def in_range(x, y) :
    if 0 <= x < n and 0 <= y < m :
        return True
    return False

def bfs(graph, target_x, target_y) :
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append([target_x, target_y])
    visited[target_x][target_y] = True
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    answer = [[0] * m for _ in range(n)]

    while queue :
        curr_x, curr_y = queue.popleft()
        for direct in range(4) :
            nx, ny = curr_x + dxs[direct], curr_y + dys[direct]
            if in_range(nx, ny) and (not visited[nx][ny]) and graph[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True
                answer[nx][ny] = answer[curr_x][curr_y] + 1

    return answer


n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

for i in range(n) :
    temp = list(map(int, input().split()))
    for j in range(m) :
        if temp[j] == 2 :
            target_x, target_y = i, j
        arr[i][j] = temp[j]

ans = bfs(arr, target_x, target_y)
for i in range(n) :
    for j in range(m) :
        if ans[i][j] == 0 :
            if arr[i][j] == 1 :
                print(-1, end=' ')
            else :
                print(0, end= ' ')
        else :
            print(ans[i][j], end = ' ')
    print()
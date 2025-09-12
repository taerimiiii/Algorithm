import sys
input = sys.stdin.readline
from collections import deque

def in_range(x, y) :
    if 0 <= x < n and 0<= y < m :
        return True
    return False

def bfs(start_x, start_y, arr, visited) :
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    answer = 0
    while queue :
        x, y = queue.popleft()
        for direct in range(4) :
            nx, ny = x + dxs[direct], y + dys[direct]
            if (not in_range(nx, ny)) or visited[nx][ny] :
                continue
            if arr[nx][ny] == 0 :
                queue.append((nx, ny))
                visited[nx][ny] = True
            elif arr[nx][ny] == 3 :
                queue.append((nx, ny))
                answer += 1
                visited[nx][ny] = True
    
    return answer

n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for i in range(n) :
    string = input()
    for j in range(m) :
        if string[j] == 'O' :
            arr[i][j] = 0
        elif string[j] == 'X' :
            arr[i][j] = 1
            visited[i][j] = True
        elif string[j] == 'I' :
            arr[i][j] = 2
            x, y = i, j
        else :
            arr[i][j] = 3


ans = bfs(x, y, arr, visited)
if ans == 0 :
    print("TT")
else :
    print(ans)
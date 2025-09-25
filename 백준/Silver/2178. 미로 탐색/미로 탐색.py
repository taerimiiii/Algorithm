import sys
input = sys.stdin.readline
from collections import deque

def dfs(map):
    queue = deque([(0, 0)])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue :
        x, y = queue.popleft()
        for direct in range(4) :
            nx, ny = x + dx[direct], y + dy[direct]
			
            if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 1 : 
                queue.append((nx, ny))
                map[nx][ny] = map[x][y] + 1

    print(map[n-1][m-1])
    return

n, m = map(int, input().split())
map = [ [0] * m for _ in range(n) ]
for i in range(n) :
    string = input()
    for j in range(m) :
        if string[j] == '1' :
            map[i][j] = 1

dfs(map)
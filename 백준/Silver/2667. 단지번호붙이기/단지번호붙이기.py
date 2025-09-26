import sys
input = sys.stdin.readline
from collections import deque

def in_range(x, y) :
    if 0 <= x < n and 0 <= y < n :
        return True
    return False

def dfs(map):
    queue = deque()
    #visited = [[False] * n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    house_counts = []

    for i in range(n) : 
        for j in range(n) :
            if map[i][j] == 1 : #
                house_cnt = 0
                queue.append([i, j])
                map[i][j] = 0

                while queue :
                    x, y = queue.popleft()
                    house_cnt += 1
                    for direct in range(4) :
                        nx, ny = x + dx[direct], y + dy[direct]
                        
                        if in_range(nx, ny) and map[nx][ny] == 1 : 
                            queue.append([nx, ny])
                            map[nx][ny] = 0

                house_counts.append(house_cnt)

    return house_counts

n = int(input())
map = [ [0] * n for _ in range(n) ]
for i in range(n) :
    string = input()
    for j in range(n) :
        if string[j] == '1' :
            map[i][j] = 1

house_cnts = dfs(map)
house_cnts.sort()

print(len(house_cnts))
for elem in house_cnts :
    print(elem)
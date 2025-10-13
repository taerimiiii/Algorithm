import sys
input = sys.stdin.readline
from collections import deque

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

n = int(input())
arr = [input().strip() for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 한 번에 적록색약 / 정상 사람 처리
dyschromatopsie = [0] * 2 #빨강-초록, 파랑
normal = [0] * 3 #빨강, 초록, 파랑

visited_dyschromatopsie = [[False] * n for _ in range(n)]
visited_normal = [[False] * n for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(n):
        if not visited_dyschromatopsie[i][j]:
            queue.append((i, j))
            visited_dyschromatopsie[i][j] = True
            color = arr[i][j]

            if color == 'R' or color == 'G':
                dyschromatopsie[0] += 1
                while queue :
                    x, y = queue.popleft()
                    for direct in range(4):
                        nx, ny = x + dx[direct], y + dy[direct]
                        
                        if in_range(nx, ny) and not visited_dyschromatopsie[nx][ny]:
                            if arr[nx][ny] == 'R' or arr[nx][ny] == 'G' :
                                visited_dyschromatopsie[nx][ny] = True
                                queue.append((nx, ny))

            else:
                dyschromatopsie[1] += 1
                while queue :
                    x, y = queue.popleft()
                    for direct in range(4):
                        nx, ny = x + dx[direct], y + dy[direct]
                        
                        if in_range(nx, ny) and not visited_dyschromatopsie[nx][ny]:
                            if arr[nx][ny] == color :
                                visited_dyschromatopsie[nx][ny] = True
                                queue.append((nx, ny))
        
        if not visited_normal[i][j]:
            queue.append((i, j))
            visited_normal[i][j] = True
            color = arr[i][j]
            
            if color == 'R':
                normal[0] += 1
                while queue :
                    x, y = queue.popleft()
                    for direct in range(4):
                        nx, ny = x + dx[direct], y + dy[direct]
                        
                        if in_range(nx, ny) and not visited_normal[nx][ny]:
                            if arr[nx][ny] == color :
                                visited_normal[nx][ny] = True
                                queue.append((nx, ny))
                                
            elif color == 'G':
                normal[1] += 1
                while queue :
                    x, y = queue.popleft()
                    for direct in range(4):
                        nx, ny = x + dx[direct], y + dy[direct]
                        
                        if in_range(nx, ny) and not visited_normal[nx][ny]:
                            if arr[nx][ny] == color :
                                visited_normal[nx][ny] = True
                                queue.append((nx, ny))

            else:
                normal[2] += 1
                while queue :
                    x, y = queue.popleft()
                    for direct in range(4):
                        nx, ny = x + dx[direct], y + dy[direct]
                        
                        if in_range(nx, ny) and not visited_normal[nx][ny]:
                            if arr[nx][ny] == color :
                                visited_normal[nx][ny] = True
                                queue.append((nx, ny))
            


print(sum(normal), sum(dyschromatopsie))
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

# 사다리
up = {}
for i in range(n) :
    x, y = map(int, input().split())
    up[x] = y

# 뱀
snake = {}
for i in range(m) :
    u, v = map(int, input().split())
    snake[u] = v

arr = [0] * 101
visited = [False] * 101
queue = deque()
queue.append(1)
visited[1] = True

while queue :
    node = queue.popleft()

    if node == 100 :
        print(arr[node])
        break

    for i in range(1, 7) :
        neighbor = node + i
        if neighbor <= 100 and not visited[neighbor] :
            if neighbor in up :
                neighbor = up[neighbor]
            elif neighbor in snake :
                neighbor = snake[neighbor]
            
            if not visited[neighbor] :
                visited[neighbor] = True
                arr[neighbor] = arr[node] + 1
                queue.append(neighbor)
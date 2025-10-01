import sys
input = sys.stdin.readline
from collections import deque

def bfs(start) :
    arr = [[0] * n for _ in range(n)]
    queue = deque()


n = int(input())
graph = {i:[] for i in range(n)}
for i in range(n) :
    arr = list(map(int, input().split()))
    for j in range(n) :
        if arr[j] == 1 :
            graph[i].append(j)

visited = [[False] * n for _ in range(n)]
for i in range(n) :
    queue = deque()
    queue.append(i)
    
    while queue :
        node = queue.popleft()
        for neighbor in graph[node] :
            if not visited[i][neighbor] :
                visited[i][neighbor] = True
                if neighbor == i :
                    continue
                queue.append(neighbor)

for i in range(n) :
    for j in range(n) :
        if visited[i][j] :
            print(1, end = ' ')
        else :
            print(0, end = ' ')
    print()
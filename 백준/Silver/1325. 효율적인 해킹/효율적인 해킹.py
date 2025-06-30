from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())

graph = [[] * n for _ in range(n)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[b-1].append(a-1)

answer = [0] * n
max_val = -1

for start in range(n) :
    visited = [0] * n
    queue = deque()

    visited[start] = 1
    queue.append(start)
    cnt = 1

    while queue :
        getout = queue.popleft()
        for elem in graph[getout] :
            if visited[elem] == 0 :
                visited[elem] = 1
                queue.append(elem)
                cnt += 1

    answer[start] = cnt
    max_val = max(max_val, cnt)


for i in range(n) :
    if answer[i] == max_val :
        print(i+1, end = ' ' )
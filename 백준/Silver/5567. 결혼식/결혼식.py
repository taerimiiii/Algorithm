import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)
visited = [False] * (n+1)
visited[1] = True
loop_cnt = 0
answer = 0

while loop_cnt < 2 and queue :
    cnt = len(queue)
    for _ in range(cnt) :
        node = queue.popleft()
        for neighbor in graph[node] :
            if not visited[neighbor] :
                queue.append(neighbor)
                visited[neighbor] = True
                answer += 1
    loop_cnt += 1

print(answer)
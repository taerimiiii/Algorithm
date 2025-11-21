import sys
from collections import deque
 
N = int(sys.stdin.readline())

graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
 
visited = [0]*(N+1) 
 
def bfs(start):
    deq = deque([start]) # 방문할 노드
    
    while deq:
        node = deq.popleft()
        
        for adj in graph[node]:
            if visited[adj] == 0:
                visited[adj] = node
                deq.append(adj)
 
bfs(1)
answer = visited[2:]
for x in answer:
    print(x)
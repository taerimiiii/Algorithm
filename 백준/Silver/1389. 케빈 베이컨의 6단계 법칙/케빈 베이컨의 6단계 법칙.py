import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, graph) :
    visited = [False] * (n+1)
    queue = deque()
    queue.append(start)
    visited[start] = True
    step_list = [0] * (n+1)

    answer = 0
    while queue :
        node = queue.popleft()
        for neighbor in graph[node] :
            if not visited[neighbor] :
                queue.append(neighbor)
                visited[neighbor] = True
                step_list[neighbor] = step_list[node] + 1
                answer += step_list[neighbor]
    
    return answer


n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m) :
    a, b = map(int, input().split())
    if a not in graph[b] :
        graph[b].append(a)
    if b not in graph[a] :
        graph[a].append(b)

min_kevin_bacon = 10 ** 9
person = 1
for start in range(1, n+1) :
    kevin_bacon = bfs(start, graph)
    #print(kevin_bacon, end=' ')
    if kevin_bacon < min_kevin_bacon :
        min_kevin_bacon = kevin_bacon
        person = start

#print()
print(person)
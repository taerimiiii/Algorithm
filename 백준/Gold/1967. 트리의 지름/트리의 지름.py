import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(node, dist) :
    for neighboor, weight in graph[node] :
        if distance[neighboor] == -1 :
            distance[neighboor] = dist + weight
            dfs(neighboor, dist + weight)

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1) :
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

if n == 1 :
    print(0)
else :
    distance = [-1] * (n+1)
    distance[1] = 0
    dfs(1, 0)
    
    far_node = distance.index(max(distance))
    
    distance = [-1] * (n+1)
    distance[far_node] = 0
    dfs(far_node, 0)
    
    print(max(distance))
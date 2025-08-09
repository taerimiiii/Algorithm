import sys
input = sys.stdin.readline
from collections import deque

def bfs(start) :
  visited = [ [0] * (n+1) for _ in range(n+1) ]
  visited[start][start] = 1

  queue = deque()
  queue.append(start)

  MAXSIZE = sys.maxsize
  dis = [MAXSIZE] * (n+1)
  prev = start
  dis[0], dis[prev] = 0, 0

  while queue :
    node = queue.popleft()
    prev = node
    
    for neighbor in graph_dict[node] :
      if visited[prev][neighbor] == 0 :
        queue.append(neighbor)
        visited[prev][neighbor] = 1
        dis[neighbor] = min(dis[neighbor], dis[prev]+graph_arr[prev][neighbor])

  return max(dis)


n = int(input())

graph_arr = [ [0] * (n+1) for _ in range(n+1)]
graph_dict = {}
for i in range(1, n+1) :
  graph_dict[i] = []

for _ in range(n-1) :
  a, b, c = map(int, input().split())
  graph_arr[a][b] = c
  graph_arr[b][a] = c
  graph_dict[a].append(b)
  graph_dict[b].append(a)

print(bfs(1))
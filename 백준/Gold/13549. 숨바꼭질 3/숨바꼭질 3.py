import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())

cnt = [0] * 100001
visited = [False] * 100001

def bfs(start, end) :
    queue = deque()
    queue.append([start, 0])
    visited[start] = True

    while queue :
        node, cnt = queue.popleft()

        if node == end :
            return cnt
        
        if 0 <= node*2 < 100001 and visited[node*2] == 0 :
            queue.appendleft([node*2, cnt])
            visited[node*2] = True

        if 0 <= node-1 < 100001 and visited[node-1] == 0 :
            queue.append([node-1, cnt+1])
            visited[node-1] = True

        if 0 <= node+1 < 100001 and visited[node+1] == 0 :
            queue.append([node+1, cnt+1])
            visited[node+1] = True

print(bfs(n,k))
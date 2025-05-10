import queue

def is_break(n, p2):
    return n == p2

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

bfs_list = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    bfs_list[x].append(y)
    bfs_list[y].append(x)

que = queue.Queue()
visited = [False] * (n + 1)

cnt = 0
que.put(p1)
visited[p1] = True
found = False

while not que.empty():
    size = que.qsize()
    
    for _ in range(size):
        current = que.get()
        if current == p2:
            found = True
            break
        for neighbor in bfs_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                que.put(neighbor)
    
    if found:
        break
    cnt += 1

print(cnt if found else -1)
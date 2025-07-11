from sys import stdin
input = stdin.readline

def tsp(curr, cnt, vals):
    global min_val
    
    if cnt == n and w[curr][0] != 0:
        min_val = min(min_val, vals + w[curr][0])
        return min_val

    if vals >= min_val:
        return 

    for _next in range(n):
        if not visited[_next] and w[curr][_next] != 0:
            visited[_next] = 1
            tsp(_next, cnt + 1, vals + w[curr][_next])
            visited[_next] = 0


n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

visited = [0] * n
visited[0] = 1
min_val = 10000000

tsp(0, 1, 0)
print(min_val)
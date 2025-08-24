import sys
input = sys.stdin.readline
from collections import deque

def dfs(level, start=0):
    global visited, v, ans, tp
    if level == n // 2:
        ans = min(ans, (v[0]**2 + v[1]**2) ** (1/2))
        return
    for i in range(start, n):
        if (visited & 1 << i) == 0:
            visited |= 1 << i
            v[0], v[1] = v[0] - arr[i][0]*2, v[1] - arr[i][1]*2
            dfs(level+1, i+1)
            v[0], v[1] = v[0] + arr[i][0]*2, v[1] + arr[i][1]*2
            visited &= ~(1 << i)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    v = [0, 0]
    ans = float("inf")
    visited = 0
    for _ in range(n):
        x, y = map(int, input().split())
        arr.append((x, y))
        v[0], v[1] = v[0] + x, v[1]+y
    dfs(0)
    print(ans)
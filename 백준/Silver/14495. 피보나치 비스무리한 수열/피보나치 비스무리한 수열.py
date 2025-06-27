from sys import stdin
input = stdin.readline

def dp(x) :
    if visited[x-1] and visited[x-3] :
        visited[x] = 1
        return fibo[x-1] + fibo[x-3]
    return dp(x-1) + dp(x-3)

n = int(input())

fibo = [1] * n
visited = [0] * n

if n > 3:
    visited[0] = 1
    visited[1] = 1
    visited[2] = 1
    for x in range(3, n) :
        fibo[x] = dp(x)

print(fibo[n-1])
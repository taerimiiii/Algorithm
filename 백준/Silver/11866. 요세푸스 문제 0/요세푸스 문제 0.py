import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

que = deque()
for i in range(1, n+1) :
    que.append(i)

answer = [0] * n
for i in range(n) :
    for _ in range(k-1) :
        temp = que.popleft()
        que.append(temp)
    answer[i] = que.popleft()

print('<', end = '')
for i in range(n-1) :
    print(answer[i], end = ', ')
print(answer[-1], end = '>')
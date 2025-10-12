import sys
input = sys.stdin.readline
from collections import deque

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

max_kinds = 0
queue = deque(arr[:k])
for i in range(n) :
    if i != 0 :  
        if i <= n/2 :
            queue.append(arr[i+k-1])
        else :
            queue.append(arr[k-(n-i)-1])
    kinds = set(queue)
    kinds.add(c)
    max_kinds = max(max_kinds, len(kinds))
    queue.popleft()

print(max_kinds)
from sys import stdin
import heapq
input = stdin.readline

n = int(input())
queue = []

for _ in range(n) :
    arr = list(map(int, input().split()))
    for elem in arr :
        if len(queue) < n :
            heapq.heappush(queue, elem)
        elif queue[0] < elem :
            heapq.heappop(queue)
            heapq.heappush(queue, elem)

print(heapq.heappop(queue))

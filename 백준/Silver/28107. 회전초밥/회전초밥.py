import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
order_list = [[] for _ in range(200001)]
for person in range(n) :
    k, *wanted = map(int, input().split())
    for want in wanted :
        heapq.heappush(order_list[want], person)
making = list(map(int, input().split()))

cnts = [0] * n
for target in making :
    if order_list[target] :
        cnts[heapq.heappop(order_list[target])] += 1

for cnt in cnts :
    print(cnt, end=' ')
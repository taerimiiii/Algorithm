import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []
for _ in range(n) :
  x = int(input())
  if x == 0 :
    if arr :
      print(heapq.heappop(arr) * (-1))
    else :
      print(0)
  else :
    heapq.heappush(arr, -x)
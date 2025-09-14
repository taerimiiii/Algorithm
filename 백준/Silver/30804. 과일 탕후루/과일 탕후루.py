import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))

start, end = 0, 0
fruits_count = defaultdict(int)
ans = 1

while start < n :
  fruits_count[arr[start]] += 1
        
  while len(fruits_count) > 2 :
    fruits_count[arr[end]] -= 1
    if fruits_count[arr[end]] == 0 :
      del fruits_count[arr[end]]
    end += 1
        
  ans = max(ans, start - end + 1)
  start += 1

print(ans)
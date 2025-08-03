import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(input().split()) for _ in range(n)]

queue = deque()
for i in range(n) :
  if arr[i][0] == "push" :
    queue.append(int(arr[i][1]))
  elif arr[i][0] == "pop" :
    if len(queue) == 0 :
      print(-1)
    else :
      print(queue[0])
      queue.popleft()
  elif arr[i][0] == "size" :
    print(len(queue))
  elif arr[i][0] == "empty" :
    if len(queue) == 0 :
      print(1)
    else :
      print(0)
  elif arr[i][0] == "front" :
    if len(queue) == 0 :
      print(-1)
    else :
      print(queue[0])
  else :
    if len(queue) == 0 :
      print(-1)
    else :
      print(queue[-1])

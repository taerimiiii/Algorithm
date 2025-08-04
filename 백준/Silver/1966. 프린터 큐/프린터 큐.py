import sys
input = sys.stdin.readline
from collections import deque

k = int(input())

for _ in range(k) :
  n, m = map(int, input().split())
  queue = deque(map(int, input().split()))

  idx, cnt = m, 0
  while 1:
    length = len(queue)
    target = queue[0]
    success = 1
    for i in range(1, length) :
      if target < queue[i] :
        queue.append(queue.popleft())
        idx = (idx + length - 1) % length
        success = 0
        break
    if success :
      queue.popleft()
      cnt += 1
      if idx == 0 :
        print(cnt)
        break
      else :
        idx = (idx + length - 1) % length

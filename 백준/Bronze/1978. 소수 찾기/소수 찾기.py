import sys
input = sys.stdin.readline
import math

n = int(input())
arr = list(map(int, input().split()))

answer = 0
for elem in arr :
  if elem == 1 :
    continue
  s = int(math.sqrt(elem)) + 1
  success = True
  for i in range(2, s) :
    if elem % i == 0 :
      success = False
      break

  if success :
    answer += 1

print(answer)
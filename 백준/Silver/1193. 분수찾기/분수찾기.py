import sys
input = sys.stdin.readline
from collections import deque

x = int(input())

n = 0
while True :
  if (n+1)*n//2 < x <= (n+2)*(n+1)//2 :
    n += 1
    break
  n += 1

abss = (n+1)*n//2 - x
if n%2 :
  print(f'{1+abss}/{n-abss}')
else :
  print(f'{n-abss}/{1+abss}')
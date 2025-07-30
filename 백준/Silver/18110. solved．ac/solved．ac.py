import sys
input = sys.stdin.readline

n = int(input())
if n == 0 :
  print(0)
else :
  arr = sorted([int(input()) for _ in range(n)])

  cut = int(n * 15 / 100 + 0.5)
  print(int(sum(arr[cut:n-cut]) / (n - 2 * cut) + 0.5))
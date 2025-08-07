import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

sum_val = 0
for i in range(n-1, -1, -1) :
  sum_val += arr[i] * (n-i)

print(sum_val)
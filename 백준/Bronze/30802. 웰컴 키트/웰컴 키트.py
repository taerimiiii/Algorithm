import sys
input = sys.stdin.readline
import math

n = int(input())
arr = map(int, input().split())
t, p = map(int, input().split())

count = 0
for elem in arr :
    if elem > 0 :
        count += math.ceil(elem / t)

print(count)
print(n // p, n % p)
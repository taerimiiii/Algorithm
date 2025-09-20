import sys
input = sys.stdin.readline

n = int(input())

k = 1
answer = 0
while n :
    if k > n :
        k = 1
    n -= k
    k += 1
    answer += 1

print(answer)
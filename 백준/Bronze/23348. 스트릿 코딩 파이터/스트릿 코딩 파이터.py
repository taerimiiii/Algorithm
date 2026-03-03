import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
n = int(input())

answer = 0
for _ in range(n) :
    sum_val = 0
    for _ in range(3) :
        x, y, z = map(int, input().split())
        sum_val += a*x + b*y + c*z
    answer = max(answer, sum_val)

print(answer)
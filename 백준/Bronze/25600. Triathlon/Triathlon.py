import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for _ in range(n) :
    a, d, g = map(int, input().split())
    score = a * (d + g)
    if a == d + g :
        score *= 2
    answer = max(answer, score)

print(answer)
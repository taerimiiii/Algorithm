import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = sorted(a+b)

for i in range(n+m) :
    print(answer[i], end=' ')

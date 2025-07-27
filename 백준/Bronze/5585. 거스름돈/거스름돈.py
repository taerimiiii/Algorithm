from sys import stdin
input = stdin.readline

n = int(input())
lift = 1000 - n

cnt = 0
coin = [500, 100, 50, 10, 5, 1]
for i in range(6) :
    while lift >= coin[i] :
        lift -= coin[i]
        cnt += 1

print(cnt)

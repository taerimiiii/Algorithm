import sys
input = sys.stdin.readline

n = int(input())
games = input().strip()

m = int(input())
targets = input().strip()

idx = n-1
answer = 0
success = True
for i in range(m) :
    target = targets[i]
    cnt = 0
    if not success :
        break
    while True :
        if cnt == n :
            success = False
            break
        idx = (idx + 1) % n
        answer += 1
        cnt += 1
        if games[idx] == target :
            break

if success :
    print(answer)
else :
    print(-1)

import sys
input = sys.stdin.readline

ps = list(map(int, input().split()))
x, y, r = map(int, input().split())

success = False
for i in range(4) :
    if ps[i] == x :
        success = True
        print(i+1)
        break

if not success :
    print(0)
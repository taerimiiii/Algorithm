import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

ans, idx, cnt = 0, 0, 0
while idx < (m - 1) :
    if s[idx:idx+3] == 'IOI' :
        idx += 2
        cnt += 1
        if cnt == n :
            ans += 1
            cnt -= 1
    else :
        idx += 1
        cnt = 0

print(ans)
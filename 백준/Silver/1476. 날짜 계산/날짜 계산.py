import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())

for i in range(1, 7982) :
    ee = i % 15
    ss = i % 28
    mm = i % 19

    if ee == 0 :
        ee = 15
    if ss == 0 :
        ss = 28
    if mm == 0 :
        mm = 19
    
    if ee == e and ss == s and mm == m :
        print(i)
        break
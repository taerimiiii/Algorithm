import sys
for _ in range(int(sys.stdin.readline())):
    tmp=[0]*10
    s=sys.stdin.readline()
    for i in range(len(s)-1):
       tmp[ int (s[i])]=1
    print(sum(tmp))
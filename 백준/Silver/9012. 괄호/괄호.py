import sys
from collections import deque
input = sys.stdin.readline

# 입력 처리
t = int(input())
queue = deque()
for _ in range(t) :
    target = input().strip()

    queue = []
    success = True
    length = len(target)
    for i in range(length) :
        if target[i] == '(' :
            queue.append(target[i])
        else :
            if queue :
                queue.pop()
            else :
                success = False
                break
    
    if queue :
        print("NO")
    elif success :
        print("YES")
    else :
        print("NO")
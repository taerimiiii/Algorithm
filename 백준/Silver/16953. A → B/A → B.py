import sys
input = sys.stdin.readline
from collections import deque

def mut(cal, prev) :
    curr = prev * 2
    if curr <= b :
        cal.append(curr)
        return cal

a, b = map(int, input().split())

stack = deque()
success = False
cnt = 1

stack.append(a)
stack.append(cnt)

while stack :
    cnt = stack.pop()
    prev = stack.pop()

    curr1 = prev * 2
    curr2 = prev * 10 + 1

    if curr1 == b or curr2 == b:
        success = True
        cnt += 1
        break

    if curr1 < b :
        stack.append(curr1)
        stack.append(cnt + 1)
    if curr2 < b :
        stack.append(curr2)
        stack.append(cnt + 1)

    #print(stack)

if success :
    print(cnt)
else :
    print(-1)
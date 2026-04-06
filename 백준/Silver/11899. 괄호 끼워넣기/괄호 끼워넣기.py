import sys
input = sys.stdin.readline
from collections import deque

s = input().strip()
length = len(s)
stack = deque()

answer = 0
for i in range(length) :
    if s[i] == ')' :
        if len(stack) == 0 :
            answer += 1
        else :
            stack.pop()
    else :
        stack.append('(')

answer += len(stack)
print(answer)
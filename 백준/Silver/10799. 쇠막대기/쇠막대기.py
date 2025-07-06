from sys import stdin
from collections import deque
input = stdin.readline

inputs = input()
length = len(inputs)
stack = deque()
cnt = 0
is_laser = 1

for i in range(length-1) :
    if inputs[i] == '(' :
        stack.append(inputs[i])
        is_laser = 1
    elif inputs[i] == ')' and is_laser :
        stack.pop()
        cnt += len(stack)
        is_laser = 0
    else :
        stack.pop()
        cnt += 1

print(cnt)
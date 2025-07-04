from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

stack = deque()
target = 1

for elem in arr :
    while stack :
        last = stack[-1]
        if last == target :
            target += 1
            stack.pop()
        else :
            break
        
    stack.append(elem)
    last = stack[-1]
    if last == target :
        target += 1
        stack.pop()

success = 1
while stack :
    last = stack.pop()
    if last == target :
        target += 1
    else :
        success = 0
        break

if success :
    print('Nice')
else :
    print('Sad')

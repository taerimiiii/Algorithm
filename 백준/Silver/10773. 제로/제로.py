import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
sum_val = 0
stack = deque()
for i in range(k) :
    num = int(input())
    if num == 0 :
        sum_val -= stack.pop()
    else :
        stack.append(num)
        sum_val += num

print(sum_val)
import sys
input = sys.stdin.readline
from collections import deque

string = input().strip()
n = len(string)
arr = []

temp = ""
for i in range(n) :
    # print(string[i])
    if string[i] == '+' or string[i] == '-' :
        if temp != "" :
            arr.append(temp)
        temp = ""
        arr.append(string[i])
    else :
        temp += string[i]

if temp != "" :
    arr.append(temp)

# print(arr)

stack = deque()
n = len(arr)
idx = 0
while idx < n :
    if arr[idx] == '+' :
        if stack :
            a = int(stack.pop())
            idx += 1
            b = int(arr[idx])
            stack.append(a + b)
    elif arr[idx] == '-' :
        if stack :
            idx += 1
            stack.append(int(arr[idx]))
        else :
            idx += 1
            stack.append(-1 * int(arr[idx]))
    else :
        stack.append(int(arr[idx]))
    idx += 1

# print(stack)

n = len(stack)
sum_val = stack[0]
for i in range(1, n) :
    sum_val -= stack[i]

print(sum_val)
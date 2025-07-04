from sys import stdin
from collections import deque
input = stdin.readline

def eng_to_val(e) :
    return ord(e) - 65

def calculate(x, y, op) :
    if op == '-' :
        return x - y
    elif op == '+' :
        return x + y
    elif op == '*' :
        return x * y
    else :
        return x / y

n = int(input())
modify = input()
values = [int(input()) for _ in range(n)]

stack = deque()
length = len(modify)

for i in range(length - 1) :
    if 'A' <= modify[i] <= 'Z' :
        stack.append(values[eng_to_val(modify[i])])
    else :
        y = stack.pop()
        x = stack.pop()
        stack.append(calculate(x, y, modify[i]))

print(f"{stack.pop():.2f}")
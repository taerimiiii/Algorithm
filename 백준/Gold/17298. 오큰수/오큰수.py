n = int(input())
arr = list(map(int, input().split()))
answer = [0] * n

NGE= [-1]*n
stack = [0]

for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        NGE[stack.pop()] = arr[i]
    stack.append(i)
print(*NGE)
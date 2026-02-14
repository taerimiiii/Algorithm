import sys
input = sys.stdin.readline

n, k = map(int, input().split())

answer = []
for _ in range(n) :
    p = int(input())
    points = list(map(int, input().split()))

    max_val = 0
    for i in range(0, 2*p, 2) :
        x = points[i]
        y = points[i+1]
        area = x**2 + y**2

        if area > max_val:
            max_val = area
    
    answer.append(max_val)

answer.sort()
print(f"{answer[k-1]:.2f}")
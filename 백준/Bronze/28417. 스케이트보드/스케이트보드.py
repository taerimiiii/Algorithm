import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for _ in range(n) :
    arr = list(map(int, input().split()))
    max_run = max(arr[:2])
    max1_t = 0
    max2_t = 0
    for elem in arr[2:] :
        if max1_t < elem :
            max2_t = max1_t
            max1_t = elem
        elif max2_t < elem :
            max2_t = elem

    max_val = max_run + max1_t + max2_t
    answer = max(answer, max_val)

print(answer)

import sys
input = sys.stdin.readline

def solution(arr, n, m):
    left, right = 0, 0
    answer = 2000000000
    while right < n:
        diff = arr[right] - arr[left]
        if diff < m:
            right += 1
        elif diff > m:
            answer = min(diff, answer)
            left += 1
        else:
            return m
    return answer    

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()
answer = solution(arr, n, m)
print(answer)
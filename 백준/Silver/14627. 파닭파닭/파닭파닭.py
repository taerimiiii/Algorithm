import sys
input = sys.stdin.readline

def binary_search(arr, target) : 
    left = 1
    right = max(arr)
    answer = 0

    while left <= right :
        mid = (left + right) // 2

        cnt = 0
        for elem in arr :
            cnt += elem // mid
        
        if cnt >= target :
            answer = max(answer, mid)
            left = mid + 1
        else :
            right = mid - 1

    return answer

s, c = map(int, input().split())
l = [int(input()) for _ in range(s)]

in_chicken = binary_search(l, c)

in_ramen = sum(l) - (in_chicken * c)

print(in_ramen)
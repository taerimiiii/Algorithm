import sys
input = sys.stdin.readline

def binary_search(L, M, left, right):
    result = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = sum(l // mid for l in L)

        if cnt >= M:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return result


M, N = map(int, input().split())
L = list(map(int, input().split()))

print(binary_search(L, M, 1, max(L)))

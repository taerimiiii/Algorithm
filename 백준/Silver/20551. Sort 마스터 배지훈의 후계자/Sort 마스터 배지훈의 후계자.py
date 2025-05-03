def binary_search_lower(target):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            # 앞서 있는 인덱스 찾기
            if right == mid :
                break
            right = mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if arr[right] == target :
        return right
    return -1

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
d = [int(input()) for _ in range(m)]

arr.sort()

for t in d :
    print(binary_search_lower(t))
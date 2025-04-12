def binary_search(left, right, target_cutting_count):
    global answer
    while left <= right:
        mid = (left + right) // 2
        cutting_count = 0
        cutting_pos = 0

        for i in range(1, M + 2):
            if arr[i] - cutting_pos >= mid:
                cutting_count += 1
                cutting_pos = arr[i]

        if cutting_count > target_cutting_count:
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1


N, M, L = map(int, input().split())
arr = [0] + [int(input()) for _ in range(M)] + [L]
arr.sort()

for _ in range(N):
    target_cutting_count = int(input())
    answer = 0
    binary_search(1, L, target_cutting_count)
    print(answer)

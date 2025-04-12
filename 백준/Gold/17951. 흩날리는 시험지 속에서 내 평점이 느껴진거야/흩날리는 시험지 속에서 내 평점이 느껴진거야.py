def binary_search(start, end):
    global k
    while start <= end:
        mid = (start + end) // 2
        sum_, group_count = 0, 0
        for s in score:
            sum_ += s
            if sum_ >= mid:
                sum_ = 0
                group_count += 1
        if group_count >= k:
            start = mid + 1
        else:
            end = mid - 1
    return end

n, k = map(int, input().split())
score = list(map(int, input().split()))

print(binary_search(0, 2000000))

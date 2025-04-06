n, m = map(int, input().split())
a = list(map(int, input().split()))

sum_val = a[0]
left = 0
right = 1
cnt = 0

while True:
    if sum_val < m:
        if right < n:
            sum_val += a[right]
            right += 1
        else:
            break
    elif sum_val == m:
        cnt += 1
        sum_val -= a[left]
        left += 1
    else:
        sum_val -= a[left]
        left += 1

print(cnt)
n = int(input())
li = list(map(int, input().split()))

left, right = 0, n - 1
minVal = abs(li[left] + li[right])
ans = [li[left], li[right]]

while left != right:
    if minVal > abs(li[left] + li[right]):
        minVal = abs(li[left] + li[right])
        ans = [li[left], li[right]]

    if li[left] + li[right] >= 0:
        right -= 1
    elif li[left] + li[right] < 0:
        left += 1

print(*ans)
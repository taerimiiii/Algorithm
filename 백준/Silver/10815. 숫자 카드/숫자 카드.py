def BinarySearch(left, right, target, have_num) :
    mid = (left + right) // 2

    while (left <= right) :
        mid = (left + right) // 2
        if target < have_num[mid] :
            right = mid - 1
        elif target > have_num[mid] :
            left = mid + 1
        elif target == have_num[mid]:
            return 1
        
    return 0

n = int(input())
have_num = list(map(int, input().split()))
m = int(input())
find_num = list(map(int, input().split()))

have_num.sort()
#print(have_num)

for i in range(m) :
    left, right = 0, n - 1
    target = find_num[i]
    output = BinarySearch(left, right, target, have_num)
    print(output, end = ' ')
    
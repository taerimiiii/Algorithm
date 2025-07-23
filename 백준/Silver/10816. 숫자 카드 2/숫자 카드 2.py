import sys
input = sys.stdin.readline

def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if result != -1 :
        return result - 1
    else :
        return result

def find_last(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


n = int(input())
nums = list(map(int, input().split()))
nums.sort()

m = int(input())
targets = list(map(int, input().split()))
for target in targets :
    #print(find_last(nums, target), find_first(nums, target), find_last(nums, target) - find_first(nums, target))
    print(find_last(nums, target) - find_first(nums, target), end = ' ')
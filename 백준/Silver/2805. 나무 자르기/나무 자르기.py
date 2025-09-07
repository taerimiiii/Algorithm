import sys
input = sys.stdin.readline

def binary_search(left, right, target) :
  while left <= right :
    mid = (left + right) // 2

    sum_val = 0
    for elem in arr :
      cut = elem - mid
      if cut > 0 :
        sum_val += cut
    
    if sum_val >= target :
      left = mid + 1
    elif sum_val < target :
      right = mid - 1

  return right

n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(binary_search(0, max(arr), m))
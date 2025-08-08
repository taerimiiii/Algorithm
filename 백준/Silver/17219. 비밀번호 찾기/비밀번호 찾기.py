import sys
input = sys.stdin.readline

def binary_search(arr, target) :
  left, right = 0, len(arr)-1
  mid = (left + right) // 2
  while left <= mid :
    if arr[mid][0] == target :
      return arr[mid][1]
    elif arr[mid][0] < target :
      left = mid + 1
    else :
      right = mid - 1
    mid = (left + right) // 2
  return 0


n, m = map(int, input().split())

arr = [list(input().split()) for _ in range(n)]
targets = [input().strip() for _ in range(m)]

arr.sort(key= lambda x : x[0])

for target in targets :
  print(binary_search(arr, target))